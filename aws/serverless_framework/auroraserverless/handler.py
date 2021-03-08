import json
import boto3
import loginit
import os

# ロガー
logger = loginit.uselogger(__name__)


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
    rdsResponse = rdsData.execute_statement(
        resourceArn=cluster_arn,
        secretArn=secret_arn,
        database=database,
        sql=query
    )
    logger.info(f'res:{rdsResponse}')

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
