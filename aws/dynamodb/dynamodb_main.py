# import os
import json
import aws.dynamodb.dynamodb_sample as mydynamo
from aws.boto3_util import createAwsServiceResource
from basic.logutil.mylogging_helper import InsertFuncLog, createDeveloplogger
import aws.myenv as myenv
import base64

logger = createDeveloplogger(__name__, 'log/debug.log')


kinesisRecodeEvents = {
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
        },
        {
            "kinesis": {
                "kinesisSchemaVersion": "1.0",
                "partitionKey": "1",
                "sequenceNumber": "49590338271490256608559692540925702759324208523137515618",
                # This is only a test.
                "data": "VGhpcyBpcyBvbmx5IGEgdGVzdC4=",
                "approximateArrivalTimestamp": 1545084711.166
            },
            "eventSource": "aws:kinesis",
            "eventVersion": "1.0",
            "eventID": "shardId-000000000006:49590338271490256608559692540925702759324208523137515618",
            "eventName": "aws:kinesis:record",
            "invokeIdentityArn": "arn:aws:iam::123456789012:role/lambda-role",
            "awsRegion": "us-east-2",
            "eventSourceARN": "arn:aws:kinesis:us-east-2:123456789012:stream/lambda-stream"
        }
    ]
}


@ InsertFuncLog(logger=logger)
def lambda_handler_kinesis(event, context):
    '''KinesisDataStreamイベントでLambdaが発火したサンプル
    公式の内容そのまま
    '''
    try:
        for record in event['Records']:
            # Kinesis data is base64 encoded so decode here
            payload = base64.b64decode(record["kinesis"]["data"])
            # bynalyで取得
            # logger.info(f"Decoded payload: {str(payload)}")
            # base64デコードで取得
            logger.info(f"Decoded payload: {payload.decode()}")
    except Exception as err:
        logger.error('エラー発生:{}'.format(err))

    return __name__ + ' Success'


@ InsertFuncLog(logger=logger)
def lambda_handler(event, context):
    try:
        resource = createAwsServiceResource(
            'dynamodb', profile=myenv.AWS_PROFILE)
        mydynamo.writedb(resource)
        mydynamo.readdb(resource)

    except Exception as err:
        logger.error('エラー発生:{}'.format(err))

    return __name__ + ' Success'


if __name__ == '__main__':
    try:

        sample_json = '{"key": "value"}'
        event = json.dumps(sample_json)

        # 疑似Lambda呼び出し
        # lambda_handler(event, '')
        lambda_handler_kinesis(kinesisRecodeEvents, '')

    except Exception as err:
        logger.error('エラー発生:{}'.format(err))
