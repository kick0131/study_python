import pprint
import cognito_helper
import cognito_auth
import os
import base64
import json
import re
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
    pprint.pprint(f'Before {token}')

    # Debug オーソライザから返せるHTTPレスポンスのパターン
    if '401' in token:
        print('=== 401 rotue ===')
        return "Unauthorized"
    if '403' in token:
        print('=== 403 rotue ===')
        return authorizerResponceV1(False)
    if '500' in token:
        print('=== 500 rotue ===')
        return "500 error"
    # if '1' in token:
    #     print('=== 401 Unauthorized ===')
    #     # 401を返す
    #     raise Exception("Unauthorized")
    # if '2' in token:
    #     print('=== 500 AUTHORIZER_ERROR ===')
    #     raise Exception("Other Error")
    # if '3' in token:
    #     print('=== 500 AUTHORIZER_CONFIGURATION_ERROR ===')
    #     return "500 error"
    # if '4' in token:
    #     print('=== 500 AUTHORIZER_CONFIGURATION_ERROR ===')
    #     return {
    #         "context": {
    #             "errmessage": "Invalid token"
    #         }
    #     }

    # RFC6750 Bearerを除いたJWT部分を抽出
    if 'Bearer' in token:
        token = re.sub(".*(Bearer) ", "", token)
    else:
        pprint.pprint('not exist Bearer')
        return authorizerResponceV1(False)
    pprint.pprint(f'After {token}')

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
    if claims is False:
        return authorizerResponceV1(False)

    # ToDo: CognitoAPIを実行し、IDトークンとアクセストークンからユーザIDを取得
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


def buildResponse(resdata: dict):
    """辞書型の内容をJSONとして返す

    # return {
    #     "resCode": resCode,
    #     "resMessage": f'resMessage[{resCode}]',
    #     "resData": resdata
    # }

    Parameters
    ----------
    resdata : dict
        オーソライザの戻り値として渡す情報

    Returns
    -------
    dict
        json形式の戻り値情報
    """
    return {k: v for k, v in resdata}


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
    policyDocument = {
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
    }
    # 後続のLambdaに渡すパラメータ
    context = {
        "key": "value",
        "numParam": 123,
        "boolParam": True
    }
    # オーソライザから返却する場合の情報
    context_res = {
        "key": "value2",
        "numParam": 456,
        "boolParam": False
    }
    b64_info = base64.b64encode(json.dumps(context).encode('utf8'))
    b64_res = base64.b64encode(json.dumps(context_res).encode('utf8'))
    policyDocument['context'] = {
        'errmessage': 'this is sample message.',
        'additional_info': b64_info.decode('utf8'),
        'additional_res': b64_res.decode('utf8')
    }

    return policyDocument


def return401():
    return "unauthorized"
