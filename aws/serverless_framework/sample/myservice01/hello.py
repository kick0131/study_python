import pprint
import loginit
import json
import base64
import pytz
from datetime import datetime

# ロガー
logger = loginit.uselogger(__name__)


def execute(event, context):
    print(f'--- {__name__} ---')
    logger.info(json.dumps(event, indent=2))

    # オーソライザからの設定値はBase64化されている
    additional_info = event['requestContext']['authorizer']['additional_info']
    additional_info = base64.b64decode(additional_info)
    additional_info = json.loads(additional_info)
    logger.info(f'== Result : {json.dumps(additional_info, indent=2)}')

    date = str(datetime.now(pytz.utc).astimezone(pytz.timezone('Asia/Tokyo')))

    msg = f'hello {date}'

    return {
        "statusCode": 200,
        "body": msg
    }


def signin(event, context):
    print(f'--- {__name__} ---')
    pprint.pprint(event)

    msg = 'SIGNIN called'

    return {
        "statusCode": 200,
        "body": msg
    }
