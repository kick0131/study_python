import json
import loginit
from boto3.session import Session
import boto3

# ロガー
logger = loginit.uselogger(__name__)


class CognitoManage:
    # boto3クライアントの生成
    # def __init__(self, profile=None):
    #     logger.info('コンストラクタ')
    #     # プロファイル指定された場合はWindows環境からと判断
    #     if(profile is not None):
    #         logger.info('プロファイル指定あり')
    #         session = Session(profile_name=profile)
    #         self.client = session.client('cognito-idp', verify=False)
    #     # プロファイル指定されなかった場合はLambdaからと判断
    #     else:
    #         logger.info('プロファイル指定なし')
    #         self.client = boto3.client('cognito-idp')
    def __init__(self):
        logger.info('プロファイル指定なし')
        self.client = boto3.client('cognito-idp')

    # サインイン（一般ユーザ）
    def signin_user(self, client_id: str, user_id: str, password: str):
        logger.info('=== SIGN IN ===')
        response = self.client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': user_id,
                'PASSWORD': password,
            },
            ClientId=client_id
        )

        logger.info('=== SIGN IN RESULT ===')
        # logger.info(response)
        logger.info(json.dumps(response, indent=2))
        return response

    # サインイン（管理者ユーザ）
    def signin_adminuser(
            self, user_pool_id: str, client_id: str,
            user_id: str, password: str):
        logger.info('=== INITIATE AUTH(ADMIN) ===')
        response = self.client.admin_initiate_auth(
            UserPoolId=user_pool_id,
            ClientId=client_id,
            AuthFlow='ADMIN_USER_PASSWORD_AUTH',
            AuthParameters={'USERNAME': user_id, 'PASSWORD': password},
        )
        logger.info('=== INITIATE AUTH(ADMIN) RESULT ===')
        logger.info(json.dumps(response))
        return response

    # サインアウト
    def global_sign_out(self, accessToken: str):
        logger.info('=== SIGN OUT ===')
        response = self.client.global_sign_out(
            AccessToken=accessToken
        )

        logger.info('=== SIGN OUT RESULT ===')
        logger.info(json.dumps(response))
        return response

    # 属性情報取得
    def get_user(self, accessToken: str):
        logger.info('=== GET USER ===')
        response = self.client.get_user(
            AccessToken=accessToken
        )

        logger.info('=== GET USER RESULT ===')
        logger.info(json.dumps(response, indent=2))
        return response

    # 属性情報取得(管理者)
    def admin_get_user(self, user_pool_id: str, user_id: str,):
        logger.info('=== GET USER(ADMIN) ===')
        response = self.client.admin_get_user(
            UserPoolId=user_pool_id,
            Username=user_id
        )

        logger.info('=== GET USER(ADMIN) RESULT ===')
        for key, val in response.items():
            logger.info(f'key:{key} val:{val}')

        return response
