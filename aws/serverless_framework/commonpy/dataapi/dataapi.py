import json
import boto3
import botocore
import loginit
import functools
import os

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


def select(query: str):
    # 環境変数の値を取得
    cluster_arn = os.environ.get("CLUSTER_ARN")
    secret_arn = os.environ.get("SECRET_ARN")
    database = os.environ.get("DATABASE")

    rdsData = boto3.client('rds-data')
    logger.info(f'{boto3.__version__}')

    logger.info(f'query:{query}')
    if query is None:
        return None

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
        raise e

    # レコード情報があればレスポンスボディに設定して返却
    body = rdsResponse['records'] if 'records' in rdsResponse else 'Empty'
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def hello():
    return "Hello World"
