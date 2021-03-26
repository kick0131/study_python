# for WSGI
from flask import Flask, jsonify, request
# for Application
import boto3
import logging
import random
import string
import datetime
import time
import base64
import json
# ログの設定
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Flask
app = Flask(__name__)

# DynamoDBオブジェクトの作成
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('datatypeSample')


@app.route("/")
def root():
    logger.info('=== root()')
    logger.info(f'event: {request.environ["serverless.event"]}')
    return "Cats"


@app.route("/cats")
def cats():
    logger.info('=== cats()')
    logger.info(f'event: {request.environ["serverless.event"]}')
    return "Cats"


@app.route("/dogs/<count>")
def dogs(count: str):
    return jsonify(
        {
            'message': 'Dogs is gone.',
            'cause': 'Not Found',
            'count': f'{count}',
            'otherType': {
                'intdata': 123,
                'booldata': True
            }
        }), 403


@app.route("/hello", methods=["POST"])
def flaskhello():

    event = request.get_json()
    logger.info(f'get_data: {event}')

    id = randomname(10)
    setid = event['id'] if 'id' in event else None
    name = event['name'] if 'name' in event else None
    action = event['action'] if 'action' in event else None
    result = {}

    if 'put' in action:
        # テーブル書き込み
        result = put(id, name)
    if 'query' in action:
        # テーブル読み込み
        result = query(id, name)
    if 'scan' in action:
        # テーブル一覧
        result = scan()
    if 'delete' in action:
        # テーブル論理削除
        delta = datetime.timedelta(seconds=10)
        result = delete(setid, name, delta)

    return jsonify({'message': f'{result}'}, 200)


def hello(event, context):

    id = randomname(10)
    setid = event['id'] if 'id' in event else None
    name = event['name'] if 'name' in event else None
    action = event['action'] if 'action' in event else None
    result = {}

    if 'put' in action:
        # テーブル書き込み
        result = put(id, name)
    if 'query' in action:
        # テーブル読み込み
        result = query(id, name)
    if 'scan' in action:
        # テーブル一覧
        result = scan()
    if 'delete' in action:
        # テーブル論理削除
        delta = datetime.timedelta(seconds=10)
        result = delete(setid, name, delta)

    response = {
        "statusCode": 200,
        "body": result
    }

    return response


def put(id, name):
    """
    DynamoDBにレコードを登録する関数
    @Param id ハッシュキー
    @Param name レンジキー
    """
    table.put_item(
        Item={
            "tenantId": id,
            "dataTypeId": name,
        }
    )


def query(id, name):
    """
    DynamoDBから検索する関数
    @Param id ハッシュキー
    @Param name レンジキー
    @return 検索結果
    """
    result = table.get_item(
        Key={
            'tenantId': id,
            'dataTypeId': name,
        }
    )
    return result


def scan():
    """
    DynamoDBから全件検索する関数
    @return 検索結果
    """
    result = table.scan()
    return result


def delete(id: str, name: str, delta: datetime.timedelta):
    """
    DynamoDBから1件論理削除する関数
    @return 削除結果
    """
    deleteAt = datetime.datetime.now() + delta
    epoc = int(time.mktime(deleteAt.timetuple()))
    # 参考
    # https://dev.classmethod.jp/articles/dynamodb-update-expression-actions/
    #
    # boto3
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.update_item
    result = table.update_item(
        Key={
            'tenantId': id,
            'dataTypeId': name
        },
        UpdateExpression="SET #attribute = :val",
        ExpressionAttributeNames={
            # UpadateExpressionで使っている#attributeを置き換える
            '#attribute': "ExpirationTime"
        },
        ExpressionAttributeValues={
            # UpadateExpressionで使っている:valを実際の値で置き換える
            ':val': epoc
        },
        # 戻り値で返す情報
        ReturnValues="UPDATED_NEW"

    )
    return result


def authhoge(event, context):
    logger.info('=== authhoge start')
    logger.info(f'event: {event}')
    policyDocument = {
        "principalId": 1,
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": "Allow",
                    "Resource": "arn:aws:execute-api:*:*:*"
                }
            ]
        },
    }
    # 後続のLambdaに渡すパラメータ
    context = {
        "key": "value",
        "numParam": 123,
        "boolParam": True
    }
    b64_info = base64.b64encode(json.dumps(context).encode('utf8'))
    policyDocument['context'] = {
        'errmessage': 'this is sample message.',
        'additional_info': b64_info.decode('utf8')
    }

    logger.info('=== authhoge end')
    return policyDocument


def randomname(n):
    """ランダム文字列の生成

    Parameters
    ----------
    n : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))
