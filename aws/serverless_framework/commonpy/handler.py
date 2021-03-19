import json
import os
import loginit

# ロガー
logger = loginit.uselogger(__name__)


def hello(event, context):

    # 環境変数の値を取得
    cluster_arn = os.environ.get("CLUSTER_ARN")
    secret_arn = os.environ.get("SECRET_ARN")
    database = os.environ.get("DATABASE")

    logger.info(f'cluster_arn : {cluster_arn}')
    logger.info(f'secret_arn : {secret_arn}')
    logger.info(f'database : {database}')

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": json.dumps(event)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
