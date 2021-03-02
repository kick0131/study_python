import json
import aws.loginit
from boto3.session import Session
import boto3

# ロガー
logger = aws.loginit.uselogger(__name__)


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
    def sign_up(self, client_id: str, user_id: str, email: str, password: str):
        logger.info('=== SIGN UP ===')
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
        logger.info('=== SIGN UP RESULT ===')
        logger.info(json.dumps(response, indent=2))
        return response

    # 一般ユーザのサインアップ承認
    def confirm_sign_up(self, client_id: str, user_id: str, confirm_code: str):
        logger.info('=== CONFIRM SIGN UP ===')
        response = self.client.confirm_sign_up(
            ClientId=client_id,
            Username=user_id,
            ConfirmationCode=confirm_code,
        )
        logger.info('=== CONFIRM SIGN UP RESULT ===')
        logger.info(json.dumps(response))
        return response

    # 管理者による承認（承認コード不要）
    def admin_confirm_sign_up(self, user_pool_id: str, user_id: str):
        logger.info('=== CONFIRM SIGN UP ===')
        response = self.client.admin_confirm_sign_up(
            UserPoolId=user_pool_id,
            Username=user_id,
        )
        logger.info('=== CONFIRM SIGN UP RESULT ===')
        logger.info(json.dumps(response))
        return response

    # 管理者ユーザのサインアップ
    def admin_create_user(
            self, user_pool_id: str, user_id: str, email: str, password: str):
        logger.info('=== SIGN UP ===')
        response = self.client.admin_create_user(
            UserPoolId=user_pool_id,
            Username=user_id,
            TemporaryPassword=password,
            UserAttributes=[{'Name': 'email', 'Value': email}],
            MessageAction='SUPPRESS'
        )
        logger.info('=== SIGN UP RESULT ===')
        logger.info(response)
        return response

    # 管理者ユーザのサインアップ承認
    def confirm_admin_user(
            self, user_pool_id: str, client_id: str,
            user_id: str, email: str, password: str):
        # ログインを試みる。（パスワードの変更を要求される。）
        logger.info('=== INITIATE AUTH ===')
        response = self.client.admin_initiate_auth(
            UserPoolId=user_pool_id,
            ClientId=client_id,
            AuthFlow='ADMIN_USER_PASSWORD_AUTH',
            AuthParameters={'USERNAME': user_id, 'PASSWORD': password},
        )
        logger.info('=== INITIATE AUTH RESULT ===')
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
        logger.info('=== PASSWORD CHANGE RESULT ===')
        logger.info(json.dumps(response))
        return response

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

    # ユーザ削除（管理者権限）
    def admin_delete_user(self, user_pool_id: str, user_id: str):
        logger.info('=== DELETE USER ===')
        response = self.client.admin_delete_user(
            UserPoolId=user_pool_id,
            Username=user_id
        )

        logger.info('=== DELETE USER RESULT ===')
        logger.info(json.dumps(response))
        return response

    # パスワード変更（管理者権限）
    def change_password(
            self, previousPassword: str,
            proposedPassword: str, accessToken: str):
        logger.info('=== CHANGE PASSWORD ===')
        response = self.client.change_password(
            PreviousPassword=previousPassword,
            ProposedPassword=proposedPassword,
            AccessToken=accessToken
        )

        logger.info('=== CHANGE PASSWORD RESULT ===')
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
        logger.info(response)
        return response

    # 属性情報取得(管理者)
    def admin_get_user(self, user_pool_id: str, user_id: str,):
        logger.info('=== GET USER(ADMIN) ===')
        response = self.client.admin_get_user(
            UserPoolId=user_pool_id,
            Username=user_id
        )

        logger.info('=== GET USER(ADMIN) RESULT ===')
        logger.info(response)
        return response

    # 属性情報更新
    def update_user_attributes(self, accessToken: str, attributes: dir):
        logger.info('=== UPDATE USER ATTRIBUTES ===')
        response = self.client.update_user_attributes(
            AccessToken=accessToken,
            UserAttributes=attributes
        )

        logger.info('=== UPDATE USER ATTRIBUTES RESULT ===')
        logger.info(json.dumps(response))
        return response

    # 属性情報更新
    def admin_update_user_attributes(
            self, user_pool_id: str, user_id: str, attributes: dir):
        logger.info('=== UPDATE USER ATTRIBUTES(ADMIN) ===')
        response = self.client.admin_update_user_attributes(
            UserPoolId=user_pool_id,
            Username=user_id,
            UserAttributes=attributes
        )

        logger.info('=== UPDATE USER ATTRIBUTES(ADMIN) RESULT ===')
        logger.info(json.dumps(response))
        return response

    # トークン更新
    def refresh_token(
            self, user_pool_id: str, client_id: str, refresh_token: str):
        logger.info('=== REFRESH TOKEN ===')
        response = self.client.initiate_auth(
            AuthFlow='REFRESH_TOKEN_AUTH',
            AuthParameters={
                'REFRESH_TOKEN': refresh_token
            },
            ClientId=client_id,
        )

        logger.info('=== REFRESH TOKEN RESULT ===')
        logger.info(json.dumps(response))
        return response

    # ユーザ一覧取得
    def list_users(self, user_pool_id: str):
        logger.info('=== LIST USERS ===')
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

        logger.info('=== LIST USERS RESULT ===')
        # logger.info(json.dumps(response))
        # return response

    # ユーザ一覧取得(再帰用)
    def list_users_ex(self, user_pool_id: str, paginationToken: str):
        logger.info('=== UPDATE USER ATTRIBUTES EX(ADMIN) ===')
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

        logger.info('=== UPDATE USER ATTRIBUTES EX(ADMIN) RESULT ===')
        # logger.info(json.dumps(response))
        # return response
