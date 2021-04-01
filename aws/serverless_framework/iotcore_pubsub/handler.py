import json
import logging

# ログの設定
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def hello(event, context):
    logger.info('=== start ===')
    logger.info(f'event:{event}')
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    logger.info('=== end ')
    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

