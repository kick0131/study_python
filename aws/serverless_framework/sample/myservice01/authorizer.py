import pprint


def lambda_handler(event, context):
    print(f'--- {__name__} ---')
    pprint.pprint(event)

    # IDトークンを期待
    token = event["headers"]["Authorization"]

    # IDトークン検証
    # ToDo: CognitoAPIを実行し、アクセストークンからユーザIDを取得

    # アクセス権限確認/属性情報取得
    # ToDo: Aurora Serverlessから必要な情報（許可URL）を取得

    # API判定
    # ToDo: 本来呼び出す先のリクエストURLが許可URLに含まれているか判定

    # ここまで到達出来たら正常
    if token == "1":
        return authorizerResponceV1(True)

    return authorizerResponceV1(False)


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
