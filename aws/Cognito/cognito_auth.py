import json
from boto3.session import Session
import boto3
from basic.logutil.mylogging_helper import InsertFuncLog, createDeveloplogger


logger = createDeveloplogger(__name__, 'log/debug.log')


def getTokenFromRes(response: dict):
    """CognitoAPIの結果からトークン情報を取り出す

    Args:
        response (dict): _description_

    Returns:
        _type_: _description_
    """
    accesstoken = response['AuthenticationResult']['AccessToken']
    refreshtoken = ''
    if 'RefreshToken' in response['AuthenticationResult']:
        refreshtoken = response['AuthenticationResult']['RefreshToken']
    idtoken = response['AuthenticationResult']['IdToken']
    return accesstoken, refreshtoken, idtoken


class CognitoManage:
    # boto3クライアントの生成
    def __init__(self, profile):
        logger.info('コンストラクタ')
        # プロファイル指定された場合はWindows環境からと判断
        if(profile is not None):
            logger.info('プロファイル指定あり')
            session = Session(profile_name=profile)
            self.client = session.client('cognito-idp', verify=False)
        # プロファイル指定されなかった場合はLambdaからと判断
        else:
            logger.info('プロファイル指定なし')
            self.client = boto3.client('cognito-idp')

    # 一般ユーザのサインアップ
    @InsertFuncLog(logger=logger)
    def sign_up(self, client_id: str, user_id: str, email: str, password: str):
        response = self.client.sign_up(
            ClientId=client_id,
            Username=user_id,
            Password=password,
            UserAttributes=[
                {
                    'Name': 'email',
                    'Value': email
                }
            ]
        )
        logger.info(json.dumps(response, indent=2))
        return response

    # 一般ユーザのサインアップ承認
    @InsertFuncLog(logger=logger)
    def confirm_sign_up(self, client_id: str, user_id: str, confirm_code: str):
        response = self.client.confirm_sign_up(
            ClientId=client_id,
            Username=user_id,
            ConfirmationCode=confirm_code,
        )
        logger.info(json.dumps(response))
        return response

    # 管理者による承認（承認コード不要）
    @InsertFuncLog(logger=logger)
    def admin_confirm_sign_up(self, user_pool_id: str, user_id: str):
        response = self.client.admin_confirm_sign_up(
            UserPoolId=user_pool_id,
            Username=user_id,
        )
        logger.info(json.dumps(response))
        return response

    # 管理者ユーザのサインアップ
    @InsertFuncLog(logger=logger)
    def admin_create_user(
            self, user_pool_id: str, user_id: str, email: str, password: str):
        response = self.client.admin_create_user(
            UserPoolId=user_pool_id,
            Username=user_id,
            TemporaryPassword=password,
            UserAttributes=[{'Name': 'email', 'Value': email}],
            MessageAction='SUPPRESS'
        )
        logger.info(response)
        return response

    # 管理者ユーザのサインアップ承認
    @InsertFuncLog(logger=logger)
    def confirm_admin_user(
            self, user_pool_id: str, client_id: str,
            user_id: str, email: str, password: str):
        # ログインを試みる。（パスワードの変更を要求される。）
        response = self.client.admin_initiate_auth(
            UserPoolId=user_pool_id,
            ClientId=client_id,
            AuthFlow='ADMIN_USER_PASSWORD_AUTH',
            AuthParameters={'USERNAME': user_id, 'PASSWORD': password},
        )
        logger.info(json.dumps(response))
        session = response['Session']

        # パスワードを変更する。
        response = self.client.admin_respond_to_auth_challenge(
            UserPoolId=user_pool_id,
            ClientId=client_id,
            ChallengeName='NEW_PASSWORD_REQUIRED',
            ChallengeResponses={'USERNAME': user_id, 'NEW_PASSWORD': password},
            Session=session
        )
        logger.info(json.dumps(response, indent=2))
        return getTokenFromRes(response)

    # サインイン（一般ユーザ）
    @InsertFuncLog(logger=logger)
    def signin_user(self, client_id: str, user_id: str, password: str):
        response = self.client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': user_id,
                'PASSWORD': password,
            },
            ClientId=client_id
        )

        logger.info(json.dumps(response, indent=2))
        return getTokenFromRes(response)

    # サインイン（管理者ユーザ）
    @InsertFuncLog(logger=logger)
    def signin_adminuser(
            self, user_pool_id: str, client_id: str,
            user_id: str, password: str):
        response = self.client.admin_initiate_auth(
            UserPoolId=user_pool_id,
            ClientId=client_id,
            AuthFlow='ADMIN_USER_PASSWORD_AUTH',
            AuthParameters={'USERNAME': user_id, 'PASSWORD': password},
        )
        logger.info(json.dumps(response, indent=2))
        return getTokenFromRes(response)

    # ユーザ削除（管理者権限）
    @InsertFuncLog(logger=logger)
    def admin_delete_user(self, user_pool_id: str, user_id: str):
        response = self.client.admin_delete_user(
            UserPoolId=user_pool_id,
            Username=user_id
        )

        logger.info(json.dumps(response))
        return response

    # パスワード変更（管理者権限）
    @InsertFuncLog(logger=logger)
    def change_password(
            self, previousPassword: str,
            proposedPassword: str, accessToken: str):
        response = self.client.change_password(
            PreviousPassword=previousPassword,
            ProposedPassword=proposedPassword,
            AccessToken=accessToken
        )

        logger.info(json.dumps(response))
        return response

    # サインアウト
    @InsertFuncLog(logger=logger)
    def global_sign_out(self, accessToken: str):
        response = self.client.global_sign_out(
            AccessToken=accessToken
        )

        logger.info(json.dumps(response))
        return response

    # 属性情報取得
    @InsertFuncLog(logger=logger)
    def get_user(self, accessToken: str):
        response = self.client.get_user(
            AccessToken=accessToken
        )

        logger.info(json.dumps(response, indent=2))
        return response

    # 属性情報取得(管理者)
    @InsertFuncLog(logger=logger)
    def admin_get_user(self, user_pool_id: str, user_id: str,):
        response = self.client.admin_get_user(
            UserPoolId=user_pool_id,
            Username=user_id
        )

        for key, val in response.items():
            logger.info(f'key:{key} val:{val}')

        return response

    # 属性情報更新
    @InsertFuncLog(logger=logger)
    def update_user_attributes(self, accessToken: str, attributes: dir):
        response = self.client.update_user_attributes(
            AccessToken=accessToken,
            UserAttributes=attributes
        )

        logger.info(json.dumps(response))
        return response

    # 属性情報更新
    @InsertFuncLog(logger=logger)
    def admin_update_user_attributes(
            self, user_pool_id: str, user_id: str, attributes: dir):
        response = self.client.admin_update_user_attributes(
            UserPoolId=user_pool_id,
            Username=user_id,
            UserAttributes=attributes
        )

        logger.info(json.dumps(response))
        return response

    # トークン更新
    @InsertFuncLog(logger=logger)
    def refresh_token(
            self, user_pool_id: str, client_id: str, refresh_token: str):
        response = self.client.initiate_auth(
            AuthFlow='REFRESH_TOKEN_AUTH',
            AuthParameters={
                'REFRESH_TOKEN': refresh_token
            },
            ClientId=client_id,
        )

        logger.info(json.dumps(response, indent=2))
        return getTokenFromRes(response)

    # ユーザ一覧取得
    @InsertFuncLog(logger=logger)
    def list_users(self, user_pool_id: str):
        response = self.client.list_users(
            UserPoolId=user_pool_id,
            Limit=1,
        )
        # 続き（PaginationToken）がある場合
        for user in response['Users']:
            if 'PaginationToken' in response:
                self.list_users_ex(user_pool_id, response["PaginationToken"])
            logger.info(f'username: {user["Username"]}')
            logger.info('attr:{}'.format(
                json.dumps(user["Attributes"], indent=2)))

        # logger.info(json.dumps(response))
        # return response

    # ユーザ一覧取得(再帰用)
    @InsertFuncLog(logger=logger)
    def list_users_ex(self, user_pool_id: str, paginationToken: str):
        response = self.client.list_users(
            UserPoolId=user_pool_id,
            PaginationToken=paginationToken,
            Limit=1,
        )
        # 続き（PaginationToken）がある場合は再起呼び出し
        for user in response['Users']:
            if 'PaginationToken' in response:
                self.list_users_ex(user_pool_id, response["PaginationToken"])
            logger.info('username:{} attr:{}'.format(
                user['Username'], user['Attributes']))

        # logger.info(json.dumps(response))
        # return response
