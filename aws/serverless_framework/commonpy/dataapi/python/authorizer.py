import base64
import json
import logging

# ログの設定
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """LanbdaLayerからオーソライザのハンドラを割り当てる為のサンプル

    本来は別のLambdaLayerで定義するので、必要最小限の実装のみ

    Parameters
    ----------
    event : [type]
        [description]
    context : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
    logger.info('=== authorizer.lambda_handler start')
    logger.info(f'event: {event}')
    policyDocument = {
        "principalId": 1,
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": "Allow",
                    "Resource": "arn:aws:execute-api:*:*:*"
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
    b64_info = base64.b64encode(json.dumps(context).encode('utf8'))
    policyDocument['context'] = {
        'errmessage': 'this is sample message.',
        'additional_info': b64_info.decode('utf8')
    }

    logger.info('=== authorizer.lambda_handler end')
    return policyDocument
