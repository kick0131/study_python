# https://aws.amazon.com/developers/getting-started/python/
import boto3
from boto3.session import Session
import base64
from botocore.exceptions import ClientError


class SecretManage:
    # boto3クライアントの生成
    def __init__(self, profile):
        # プロファイル指定された場合はWindows環境からと判断(.aws/credential)
        if(profile is None):
            session = Session(profile_name=profile)
            self.client = session.client('secretsmanager', verify=False)
        # プロファイル指定されなかった場合はLambdaからと判断
        else:
            self.client = boto3.client('secretsmanager')

    # secret_name : SecretManagerのシークレットキー
    def get_secret(self, secret_name: str):

        try:
            get_secret_value_response = self.client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            ERR_INTERNALSERVICE = 'InternalServiceErrorException'
            if e.response['Error']['Code'] == 'DecryptionFailureException':
                raise e
            elif e.response['Error']['Code'] == ERR_INTERNALSERVICE:
                raise e
            elif e.response['Error']['Code'] == 'InvalidParameterException':
                raise e
            elif e.response['Error']['Code'] == 'InvalidRequestException':
                raise e
            elif e.response['Error']['Code'] == 'ResourceNotFoundException':
                raise e
        else:
            # Decrypts secret using the associated KMS CMK.
            # Depending on whether the secret is a string or binary,
            # one of these fields will be populated.
            if 'SecretString' in get_secret_value_response:
                secret = get_secret_value_response['SecretString']
            else:
                decoded_binary_secret = base64.b64decode(
                    get_secret_value_response['SecretBinary'])
                print(decoded_binary_secret)

        # Your code goes here.
        assert(secret)
        return secret
