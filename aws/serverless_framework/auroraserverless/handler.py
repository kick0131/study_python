import json
import boto3
import botocore
import loginit
import os
import functools
import re

# ロガー
logger = loginit.uselogger(__name__)


def InsertFuncLog(func):
    """メソッドの開始と終わりのログを付与するデコレータ

    Parameters
    ----------
    func : function
        デコレータ対象のメソッド

    Returns
    -------
    function
        デコレートされたメソッド
    """
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        logger.info(f'=== {func.__name__} start')
        result = func(*args, **kwargs)
        logger.info(f'=== {func.__name__} end')
        return result
    return _wrapper


@InsertFuncLog
def parse_dataapiresult_to_list(dataapiresult: dict):
    newlist = []
    for listitems in dataapiresult:
        locallist = []
        for dicitem in listitems:
            # logger.info(f'check 3 {dicitem}')
            for value in dicitem.values():
                locallist.append(value)
        newlist.append(locallist)
    return newlist


@InsertFuncLog
def parse_dataapiresult_to_list2(dataapiresult: dict):
    """[summary]

    ⭐️ToDo ジェネレータやリスト内包表記でもっと上手くかけるはず。。。
    itertoolsモジュールを検討
    https://note.nkmk.me/python-list-comprehension/

    Parameters
    ----------
    dataapiresult : dict
        [description]

    Returns
    -------
    [type]
        [description]
    """
    newlist = []
    logger.info('check 1')

    it = (x for x in dataapiresult)
    for item in it:
        logger.info(f'it:{item}')
    it2 = (x for x in it)
    for item in it2:
        logger.info(f'it2:{item}')
    it3 = (x for x in it2)
    for item in it3:
        logger.info(f'it3:{item}')
    it4 = (x for x in it3)
    for item in it4:
        logger.info(f'it4:{item}')

    for listitems in dataapiresult:
        logger.info(f'check 2 type:{type(listitems)} {listitems}')
        # sample = [x.values() in x for listitems]
        # logger.info(f'sample:{sample}')
        # locallist = []
        # for dicitem in listitems:
        #     logger.info(f'check 3 {dicitem}')
        #     for value in dicitem.values():
        #         locallist.append(value)
        # newlist.append(locallist)
    return newlist


def checkAllowApi(allowlist, method, url):
    """APIの許可リストに一致しているかをチェックする

    チェックリストはワイルドカードとしてアスタリスクが使用可能
    それ以外は後方完全一致でチェックする

    ex)操作対象とチェックOKになるパターン
    /api/
        http://XXXX                X
        http://XXXX/               X
        http://XXXX/api            X
        http://XXXX/api/           O
        http://XXXX/api/XXXX/api   X
        http://XXXX/api/XXXX/api/  O
        http://XXXX/api/XXXX       X
        http://XXXX/api/XXXX/      X
    /api/*
        http://XXXX                X
        http://XXXX/               X
        http://XXXX/api            X
        http://XXXX/api/           O
        http://XXXX/api/XXXX/api   O
        http://XXXX/api/XXXX/api/  O
        http://XXXX/api/XXXX       O
        http://XXXX/api/XXXX/      O

    Parameters
    ----------
    allowlist : array list
        サービスエイリアスマスタから取得した「操作」「操作対象」のセット
    method : str
        HTTPメソッド
    url : str
        リクエストURL
     """
    umethod = method.upper()
    logger.info(f'ARG {umethod} {url}')

    # ドメイン部分 ToDo:環境変数対応
    DOMAIN = 'http://XXXX'

    # 条件にマッチするものがあれば即Trueを返却
    methods = (x[1] for x in allowlist)
    apis = (x[2] for x in allowlist)
    for method, api in zip(methods, apis):
        logger.info(f'{method} {api}')
        # methodチェック
        if method.upper() == umethod:
            # 操作対象が不正フォーマットの場合はチェック無効 ToDo:実装

            # 末尾にアスタリスクがある場合はワイルドカード(正規表現の.*)として判定
            api = regexReplaceWildCard(api)

            # urlチェック
            content = url
            pattern = '^'+DOMAIN+api+'$'
            logger.debug(f'pattern:{pattern} context:{content}')
            if regextest(pattern, content) is not None:
                return True
    return False


def regexReplaceWildCard(msg):
    """末尾がアスタリスクの場合、正規表現のワイルドカードに置換する

    Parameters
    ----------
    msg : str
        置換対象のメッセージ

    Returns
    -------
    str
        置換結果、置換されなかった場合は入力メッセージがそのまま返される
    """
    if isLastAsterisc(msg):
        # 任意の文字列＋末尾アスタリスク
        return msg[:len(msg)-1] + '.*'
    return msg


def isLastAsterisc(msg):
    if not msg:
        return False
    return msg[len(msg)-1:] == '*'


def regextest(pattern, content):
    regex = re.compile(pattern)
    return regex.match(content)


def hello(event, context):

    # 環境変数の値を取得
    cluster_arn = os.environ.get("CLUSTER_ARN")
    secret_arn = os.environ.get("SECRET_ARN")
    database = os.environ.get("DATABASE")

    rdsData = boto3.client('rds-data')
    logger.info(f'{boto3.__version__}')

    # 引数にクエリ文字があれば設定
    query = event['query'] if 'query' in event else None
    logger.info(f'query:{query}')
    if query is None:
        body = {
            "message": "arg query is None.",
            "input": event
        }

        errresponse = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        return errresponse

    # DataAPI実行
    try:
        rdsResponse = rdsData.execute_statement(
            resourceArn=cluster_arn,
            secretArn=secret_arn,
            database=database,
            sql=query
        )
        logger.info(f'res:{rdsResponse}')
    except botocore.exceptions.ClientError as e:
        logger.error(f'exception:{e}')
        # APIリファレンスにある例外は以下の形で判定する
        # RDSDataService.Client.exceptions.BadRequestException
        #
        # RDSDataService.Client.XXXXXというインスタンスがあるわけではない点、注意
        #
        if e.response['Error']['Code'] == 'BadRequestException':
            logger.error('=== BadRequestException')
        if e.response['Error']['Code'] == 'StatementTimeoutException':
            logger.error('=== StatementTimeoutException')
        if e.response['Error']['Code'] == 'InternalServerErrorException':
            logger.error('=== InternalServerErrorException')
        if e.response['Error']['Code'] == 'ForbiddenException':
            logger.error('=== ForbiddenException')
        if e.response['Error']['Code'] == 'ServiceUnavailableError':
            logger.error('=== ServiceUnavailableError')
        return None

    # レコード情報があればレスポンスボディに設定して返却
    body = rdsResponse['records'] if 'records' in rdsResponse else 'Empty'
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """


# -------------------------------------------------------------------
# main
# -------------------------------------------------------------------
# TestData
records = [
    [
        {
            "stringValue": "user-read"
        },
        {
            "stringValue": "GET"
        },
        {
            "stringValue": "/mng/"
        }
    ],
    [
        {
            "stringValue": "user-read"
        },
        {
            "stringValue": "POST"
        },
        {
            "stringValue": "/mng/*"
        }
    ]
]


def main():
    selectresult = parse_dataapiresult_to_list(records)
    logger.info(selectresult)
    urlpattern = [
        'http://XXXX/mng/',
        'http://XXXX/mng/ABCDE',
    ]
    method = 'get'
    for url in urlpattern:
        isApiAllow = checkAllowApi(selectresult, method, url)
        logger.info(f'url:{url} check:{isApiAllow}')


if __name__ == '__main__':
    try:
        # logger.info(regextest('^http://XXXXX/mng/$', 'http://XXXXX/mng/a'))
        # logger.info(isLastAsterisc('aa*'))
        # logger.info(regexReplaceWildCard('aa*a'))
        main()

    except Exception as err:
        logger.error('エラー発生:{}'.format(err))
