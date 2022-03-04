import base64
import json
from basic.logutil.mylogging_helper import createDeveloplogger, InsertFuncLog

logger = createDeveloplogger(__name__, 'log/debug.log')

"""base64モジュールの使い方

    == 基本
    文字列からバイト型への変換
    str.encode()

    バイト型から文字列への変換
    byte.decode()

"""

# Kinesisレコードイベント
kinesis_record = {
    "Records": [
        {
            "kinesis": {
                "kinesisSchemaVersion": "1.0",
                "partitionKey": "1",
                "sequenceNumber": "49590338271490256608559692538361571095921575989136588898",
                # Hello, this is a test.
                "data": "SGVsbG8sIHRoaXMgaXMgYSB0ZXN0Lg==",
                "approximateArrivalTimestamp": 1545084650.987
            },
            "eventSource": "aws:kinesis",
            "eventVersion": "1.0",
            "eventID": "shardId-000000000006:49590338271490256608559692538361571095921575989136588898",
            "eventName": "aws:kinesis:record",
            "invokeIdentityArn": "arn:aws:iam::123456789012:role/lambda-role",
            "awsRegion": "us-east-2",
            "eventSourceARN": "arn:aws:kinesis:us-east-2:123456789012:stream/lambda-stream"
        }
    ]
}

# サンプルデータ
context = {
    "key": "value",
    "numParam": 123,
    "boolParam": True
}

@InsertFuncLog(logger=logger)
def b64encode(message: str):
    bytedata = message.encode()
    logger.info('--- base64encode ---')
    logger.info(f'normal : {base64.b64encode(bytedata)}')
    logger.info(f'urlsafe: {base64.urlsafe_b64encode(bytedata)}')
    return base64.b64encode(bytedata)


@InsertFuncLog(logger=logger)
def b64decode(bytedata: bytes):
    logger.info('--- base64decode ---')
    logger.info(f'normal : {base64.b64decode(bytedata)}')
    logger.info(f'urlsafe: {base64.urlsafe_b64decode(bytedata)}')


@InsertFuncLog(logger=logger)
def jsonencode():


    # base64化
    b64_info = base64.b64encode(json.dumps(context).encode('utf8'))
    logger.info(f'b64_info   : {b64_info} type: {type(b64_info)}')
    # byte -> str
    # 注意！！末尾にカンマがあるとtuple扱いになる
    # b64_decode = b64_info.decode('utf8'),
    b64_decode = b64_info.decode('utf8')
    logger.info(f'b64_decode : {b64_decode} type: {type(b64_decode)}')


def kinesisEventWithJson(body: dict) -> dict:
    """Kinesisイベント生成

    bodyにjsonデータが含まれるKinesisイベントを作成する。

    以下の使い方を想定
    kinesisevent = kinesisEventWithJson(jsondata)
    lambda_handler(kinesisevent, context)

    .. note::

        KinesisのdataフィールドはBase64エンコード文字列を設定する決まりがある

    Args:
        body (dict): Kinesisレコードのdata部に設定するjson

    Returns:
        dict: Kinesisレコード
    """
    kinesis_record['Records'][0]['kinesis']['data'] = dictToBase64Str(body)
    return kinesis_record


def dictToBase64Str(body: dict) -> str:
    """dictをBase64文字列に変換

    jsonのシリアライズ

    Args:
        body (dict): Base64化したいデータ

    Returns:
        str: Base64変換した文字列
    """
    return base64.b64encode(json.dumps(body).encode()).decode()


if __name__ == '__main__':
    encoded = b64encode('abcde')
    b64decode(encoded)
    jsonencode()
    logger.info(dictToBase64Str(context))
