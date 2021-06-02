import os
import aws.loginit
import json
from aws.cognito.cognito_auth import CognitoManage

# 本ファイルは固有情報がある為、非公開

# AWSプロファイル未使用の場合は空文字とする
awsprofile = 'awsdcpf'


def lambda_handler(event, context):
    """汎用Lambdaハンドラモジュール
    """

    # TODO implement
    client_id = event['client_id']
    user_id = event['user_id']
    email = event['email']
    password = event['password']
    # password2 = event['password2']
    # confirm_code = event['confirm_code']
    user_pool_id = event['user_pool_id']
    accesstoken = event['accesstoken']
    # refreshtoken = event['refreshtoken']
    # pagenationtoken = event['pagenationtoken']
    # attributes = event['attributes']

    # 引数eventの内容表示
    logger.info(json.dumps(event, indent=2))

    # 引数なしの場合はデフォルトプロファイル
    if len(awsprofile) != 0:
        cognitoclass = CognitoManage(awsprofile)
    else:
        cognitoclass = CognitoManage()

    # 動作確認OK
    # サインアップ（一般ユーザ）
    # cognitoclass.sign_up(client_id, user_id, email, password)
    # 承認
    # cognitoclass.confirm_sign_up(client_id,user_id,confirm_code)

    # 管理者権限の承認
    # cognitoclass.admin_confirm_sign_up(user_pool_id,user_id)

    # 管理者権限のユーザ削除
    # cognitoclass.admin_delete_user(user_pool_id,user_id)

    # サインイン（一般ユーザ）
    # res = cognitoclass.signin_user(client_id, user_id, password)
    # if len(accesstoken) == 0:
    #     accesstoken = res['AuthenticationResult']['AccessToken']
    #     logger.info(accesstoken)

    # サインアップ（管理者）
    cognitoclass.admin_create_user(user_pool_id, user_id, email, password)
    cognitoclass.confirm_admin_user(
        user_pool_id, client_id, user_id, email, password)

    # サインイン（管理者）
    # cognitoclass.signin_adminuser(user_pool_id, client_id, user_id, password)

    # パスワード変更
    # cognitoclass.change_password(password, password2, accesstoken)

    # サインアウト
    # cognitoclass.global_sign_out(accesstoken)

    # 属性情報更新
    # cognitoclass.update_user_attributes(accesstoken, attributes)

    # 属性情報更新
    # cognitoclass.admin_update_user_attributes(
    # user_pool_id, user_id, attributes)

    # 属性情報取得(カスタム属性が取得出来ないので使用しない)
    # cognitoclass.get_user(accesstoken)

    # 属性情報取得
    # cognitoclass.admin_get_user(user_pool_id, user_id)

    # トークン更新
    # cognitoclass.refresh_token(user_pool_id, client_id, refreshtoken)

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
        logger = aws.loginit.uselogger(__name__)

        logger.debug('テスト')

        # オープンするファイルは非公開
        json_open = open((os.path.dirname(__file__)
                          + '/../_privatejson/cognito_data_dcpf.json'), 'r')
        event = json.load(json_open)
        lambda_handler(event, '')

    except Exception as err:
        logger.error('エラー発生:{}'.format(err))
