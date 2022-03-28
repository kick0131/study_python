import json
from aws.cognito.cognito_auth import CognitoManage
import aws.myenv as myenv
from basic.logutil.mylogging_helper import InsertFuncLog, createDeveloplogger


logger = createDeveloplogger(__name__, 'log/debug.log')

client_id = myenv.COGNITO_CLIENT_ID
user_id = myenv.COGNITO_USER_ID
email = myenv.COGNITO_EMAIL
password = myenv.COGNITO_PASSWORD
user_pool_id = myenv.COGNITO_USER_POOL_ID
accesstoken = ""

# 引数なしの場合はデフォルトプロファイル
if len(myenv.AWS_PROFILE) != 0:
    cognitoclass = CognitoManage(myenv.AWS_PROFILE)
else:
    cognitoclass = CognitoManage()


@InsertFuncLog(logger=logger)
def signup_pre():
    """一般権限のサインアップ

    仮登録状態となり、email宛に検証コードが送信される
    """
    cognitoclass.sign_up(client_id, user_id, email, password)


@InsertFuncLog(logger=logger)
def user_confirm(confirm_code: str):
    """一般権限のサインアップ承認シーケンス

    一般権限のサインアップ正常終了後、
    emailで検証コードが送られてくるのでその検証コードを使用し、承認シーケンスを実行する

    Args:
        confirm_code (str): emailで送られてきた検証コード
    """
    cognitoclass.confirm_sign_up(client_id, user_id, confirm_code)


@InsertFuncLog(logger=logger)
def sign_in(admin=False):
    """サインイン

    Args:
        user_pool_id (str, optional): ユーザプールID、管理者メソッド時のみ必要.
        admin (bool, optional): 管理者メソッドを使用するか.
    """
    if admin:
        # サインイン（管理者）
        # ALLOW_ADMIN_USER_PASSWORD_AUTHが必要
        return cognitoclass.signin_adminuser(
            user_pool_id, client_id, user_id, password)

    else:
        # サインイン（一般ユーザ）
        # USER_PASSWORD_AUTHが必要
        return cognitoclass.signin_user(
            client_id, user_id, password)


@InsertFuncLog(logger=logger)
def get_attr(accesstoken: str = "", admin=False):
    """属性情報取得

    管理者メソッド使用時のみカスタム属性を取得可能

    Args:
        accesstoken (str, optional): アクセストークン. Defaults to "".
        admin (bool, optional): 管理者メソッドを使用するか. Defaults to False.
    """
    if admin:
        cognitoclass.admin_get_user(user_pool_id, user_id)

    else:
        cognitoclass.get_user(accesstoken)


@InsertFuncLog(logger=logger)
def one_pass():
    """一連動作

    ユーザ生成
    サインイン
    属性情報取得(アクセストークン使用例)
    サインアウト
    ユーザ削除
    """
    # ユーザ生成
    cognitoclass.admin_create_user(user_pool_id, user_id, email, password)
    accesstoken, refreshtoken, idtoken = cognitoclass.confirm_admin_user(
        user_pool_id, client_id, user_id, email, password)

    # サインイン
    sign_in()

    # 属性情報取得
    get_attr(accesstoken=accesstoken)

    # サインアウト
    cognitoclass.global_sign_out(accesstoken)

    # ユーザ削除
    cognitoclass.admin_delete_user(user_pool_id, user_id)


@InsertFuncLog(logger=logger)
def customize_execute(event, context):
    """汎用Lambdaハンドラモジュール
    """

    # 引数eventの内容表示
    # logger.info(json.dumps(event, indent=2))

    # 管理者権限のユーザ削除
    # cognitoclass.admin_delete_user(user_pool_id,user_id)

    # サインイン（一般ユーザ）
    # USER_PASSWORD_AUTHが必要
    accesstoken, refreshtoken, idtoken = cognitoclass.signin_user(
        client_id, user_id, password)

    # サインアップ（管理者）
    # cognitoclass.admin_create_user(user_pool_id, user_id, email, password)
    # accesstoken, refreshtoken, idtoken = cognitoclass.confirm_admin_user(
    #     user_pool_id, client_id, user_id, email, password)

    # サインイン（管理者）
    # ALLOW_ADMIN_USER_PASSWORD_AUTHが必要
    # accesstoken, refreshtoken, idtoken= cognitoclass.signin_adminuser(
    #     user_pool_id, client_id, user_id, password)

    # パスワード変更
    # cognitoclass.change_password(password, password2, accesstoken)

    # サインアウト
    # cognitoclass.global_sign_out(accesstoken)

    # 属性情報更新
    # cognitoclass.update_user_attributes(accesstoken, attributes)

    # 属性情報更新
    # cognitoclass.admin_update_user_attributes(
    # user_pool_id, user_id, attributes)

    # トークン更新
    # リフレッシュトークンは更新されない為、返却しない
    accesstoken, _, idtoken = cognitoclass.refresh_token(
        user_pool_id, client_id, refreshtoken)

    # ユーザ一覧
    # cognitoclass.list_users(user_pool_id)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


# -------------------------------------------------------------------
# main
# -------------------------------------------------------------------
if __name__ == '__main__':
    try:
        logger.debug('== Cognito Sample Start==')

        # 一連動作
        one_pass()

        # 個別に動きを見たい場合
        # customize_execute({}, '')

    except Exception as err:
        logger.error('エラー発生:{}'.format(err))
