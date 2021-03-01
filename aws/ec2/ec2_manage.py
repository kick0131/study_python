import sys
import boto3
from boto3.session import Session
from botocore.exceptions import ClientError
import aws.loginit

logger = aws.loginit.uselogger(__name__)


class EC2Manage:
    # boto3クライアントの生成
    def __init__(self, profile=None):
        logger.info('コンストラクタ')
        # プロファイル指定された場合はWindows環境からと判断
        if(profile is not None):
            session = Session(profile_name=profile)
            self.client = session.client('ec2', verify=False)
        # プロファイル指定されなかった場合はLambdaからと判断
        else:
            self.client = boto3.client('ec2')

    def startstopEC2(self, ec2InstanceIds, action):
        """EC2インスタンスの開始・停止

        ec2InstanceIds                    :操作対象のインスタンスIDを表すList型
        action                            :EC2に対する操作  'start'|'stop'
        """
        logger.debug('=== [{}] start ==='.format(
            sys._getframe().f_code.co_name))

        try:
            if action == 'start':
                response = self.client.start_instances(
                    InstanceIds=ec2InstanceIds)
            elif action == 'stop':
                response = self.client.stop_instances(
                    InstanceIds=ec2InstanceIds)
            else:
                raise Exception('actionを指定して下さい')
            logger.debug(f'=== {response}')

        except ClientError as e:
            logger.error(e)

        logger.debug('=== [{}] end ==='.format(sys._getframe().f_code.co_name))
