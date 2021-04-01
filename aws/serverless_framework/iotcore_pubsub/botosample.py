import boto3
import botocore
import json
import logging

MESSAGE = "Hello World"
TOPIC = "test/testing"
QOS = 1

# ログの設定
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def publish(event: object, context: object):
    """IoTCoreにPublishメッセージを送信します

    Args:
        event (object): [description]
        context (object): [description]
    """
    logger.info('=== PUBLISH ===')
    logger.info(f'boto3: {boto3.__version__} botocore:{botocore.__version__}')

    client = boto3.client('iot-data')

    payload = {
        'message': MESSAGE
    }
    try:
        response = client.publish(
            topic=TOPIC,
            qos=QOS,
            payload=json.dumps(payload, ensure_ascii=False)
        )
    except botocore.exceptions.ClientError as e:
        logger.error('{e}')
        if e.response['Error']['Code'] == 'InternalFailureException':
            logger.error('=== InternalFailureException')
        if e.response['Error']['Code'] == 'InvalidRequestException':
            logger.error('=== InvalidRequestException')
        if e.response['Error']['Code'] == 'UnauthorizedException':
            logger.error('=== UnauthorizedException')
        if e.response['Error']['Code'] == 'MethodNotAllowedException':
            logger.error('=== MethodNotAllowedException')
        raise e

    logger.info(f'response: {response}')

    logger.info('=== PUBLISH END ===')
    return response
