# import os
import json
import aws.dynamodb.dynamodb_sample as mydynamo
from aws.boto3_util import createAwsServiceResource
from basic.logutil.mylogging_helper import InsertFuncLog, createDeveloplogger
import aws.myenv as myenv

logger = createDeveloplogger(__name__, 'log/debug.log')


@InsertFuncLog(logger=logger)
def lambda_handler(event, context):
    try:
        resource = createAwsServiceResource('dynamodb', profile=myenv.AWS_PROFILE)
        # mydynamo.writedb(resource)
        mydynamo.readdb(resource)

    except Exception as err:
        logger.error('エラー発生:{}'.format(err))

    return __name__ + ' Success'


if __name__ == '__main__':
    try:

        sample_json = '{"key": "value"}'
        event = json.dumps(sample_json)

        # 疑似Lambda呼び出し
        lambda_handler(event, '')

    except Exception as err:
        logger.error('エラー発生:{}'.format(err))
