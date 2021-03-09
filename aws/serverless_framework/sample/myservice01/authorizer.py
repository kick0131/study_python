import pprint
import cognito_helper
import cognito_auth
import os
# オーソライザー連携を行っているため、ローカル実行時など、使用しない場合はコメントアウト
# Use decode-verify-jwt.py on Lambda Layer
# https://github.com/awslabs/aws-support-tools/blob/master/Cognito/decode-verify-jwt/decode-verify-jwt.py
import decodeverifyjwt

# Lambda環境変数からユーザプールIDを取得
user_pool_id = os.getenv('USER_POOL_ID')
user_id = os.getenv('USER_ID')


def lambda_handler(event, context):
    print(f'--- {__name__} ---')
    pprint.pprint(event)

    # IDトークンを期待
    token = event["headers"]["Authorization"]

    # DEBUG CognitoIDトークンからユーザ名を取得
    payload = cognito_helper.parse_idtoken(token)
    decodedpayload = cognito_helper.decode_idtoken(payload)
    print(f'username: {decodedpayload["cognito:username"]}')

    # IDトークン検証
    # LambdaLayerのトークン検証モジュールを呼び出し
    print('Start ID token verify')
    veryfyInput = {'token': token}
    claims = decodeverifyjwt.lambda_handler(veryfyInput, None)
    print(f'claims : {claims}')

    # ToDo: CognitoAPIを実行し、アクセストークンからユーザIDを取得
    # user_pool_id = "ap-northeast-1_TfjuIRFBa"
    # user_id = "test"
    print('Call CognitoAPI')
    cognito = cognito_auth.CognitoManage()
    attr = cognito.admin_get_user(user_pool_id, user_id)
    pprint.pprint(attr)

    # アクセス権限確認/属性情報取得
    # ToDo: Aurora Serverlessから必要な情報（許可URL）を取得

    # API判定
    # ToDo: 本来呼び出す先のリクエストURLが許可URLに含まれているか判定

    # ここまで到達出来たら正常
    return authorizerResponceV1(True)


def authorizerResponceV1(isAllow: bool):
    """バージョン１形式のポリシードキュメント生成メソッド

    Parameters
    ----------
    isAllow : bool
        認証結果に対応したポリシーの設定値
        true :後続のLambda実行を許可するポリシーを応答
        false:後続のLambda実行を拒否するポリシーを応答

    Returns
    -------
    dict
        AWS準拠のポリシードキュメント
    """
    effect = "Allow" if isAllow is True else "Deny"
    return {
        "principalId": 1,
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": "arn:aws:execute-api:*:*:*/*/*/"
                }
            ]
        },
        # 後続のLambdaに渡すパラメータ
        "context": {
            "key": "value",
            "numParam": 123,
            "boolParam": True
        }
    }
