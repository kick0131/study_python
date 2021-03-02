import pprint


def lambda_handler(event, context):
    print(f'--- {__name__} ---')
    pprint.pprint(event)

    token = event["headers"]["Authorization"]
    if token == "1":
        return authorizerResponceV1(True)

    return authorizerResponceV1(False)
    # return {
    #     "principalId": 1,
    #     "policyDocument": {
    #         "Version": "2012-10-17",
    #         "Statement": [
    #             {
    #                 "Action": "*",
    #                 "Effect": "Deny",
    #                 "Resource": "arn:aws:execute-api:*:*:*/*/*/"
    #             }
    #         ]
    #     }
    # }


def authorizerResponceV1(isAllow: bool):
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


def authorizerResponceV2():
    return {
        "isAuthorized": True,
        "context": {
            "Discription": "this is sample",
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "*",
                    "Effect": "Allow",
                    "Resource": "arn:aws:execute-api:*:*:*/*/*/"
                }
            ]
        }
    }
