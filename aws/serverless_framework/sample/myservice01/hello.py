import pprint
import pytz
from datetime import datetime


def execute(event, context):
    print(f'--- {__name__} ---')
    pprint.pprint(event)
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
