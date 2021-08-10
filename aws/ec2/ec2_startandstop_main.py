import os
import json
from aws.ec2.ec2_manage import EC2Manage
import aws.loginit


def lambda_handler(event, context):
    try:
        # 引数はAWSプロファイル名
        ec2obj = EC2Manage('hira')
        instanceIds = event['startaction']['instanceIds']
        action = 'stop'

        ec2obj.startstopEC2(instanceIds, action)

    except Exception as err:
        logger.error('エラー発生:{}'.format(err))

    return __name__ + ' Success'


if __name__ == '__main__':
    try:
        logger = aws.loginit.uselogger(__name__)

        # 操作対象のインスタンスID
        # オープンするファイルは非公開
        json_open = open((os.path.dirname(__file__)
                          + '/../_privatejson/ec2_data.json'), 'r')
        event = json.load(json_open)

        logger.debug('EC2instanceid:{}'.format(event))

        # EC2インスタンス操作
        lambda_handler(event, '')

    except Exception as err:
        logger.error('エラー発生:{}'.format(err))
