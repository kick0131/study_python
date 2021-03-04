import pprint
import pytz
from datetime import datetime


def lambda_handler(event, context):
    print(f'--- {__name__} ---')
    pprint.pprint(event)
    date = str(datetime.now(pytz.utc).astimezone(pytz.timezone('Asia/Tokyo')))

    msg = f'hello {date}'

    return {
        "statusCode": 200,
        "body": msg
    }
