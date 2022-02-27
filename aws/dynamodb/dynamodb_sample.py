# from botocore.exceptions import ClientError
from basic.logutil.mylogging_helper import InsertFuncLog, createDeveloplogger
from datetime import datetime, timezone, timedelta
import aws.myenv as myenv

logger = createDeveloplogger(__name__, 'log/debug.log')

UTC = timezone.utc
JST = timezone(timedelta(hours=+9), 'JST')
TABLENAME = myenv.DYNAMODB_TABLE


@InsertFuncLog(logger=logger)
def formatdatetimeSample(dt: datetime):
    """フォーマット指定の時刻取得

    書式指定
    https://docs.python.org/ja/3/library/datetime.html#strftime-and-strptime-behavior

    Parameters
    ----------
    dt : datetime
        [description]
    """
    TimeFmt = '%Y/%m/%dT%H:%M:%S%z'

    # 初期値
    logger.info(f'before        : {dt}')

    # Timezone指定あり
    newdt = datetime.fromtimestamp(dt.timestamp(), JST)
    return newdt.strftime(TimeFmt)


@InsertFuncLog(logger=logger)
def writedb(resource):
    table = resource.Table(TABLENAME)
    response = table.put_item(
        Item={
            # 'sensorId': '2015',
            'CreatedId': '2015',
            'getDataTime': formatdatetimeSample(datetime.now()),
            'info': {
                'plot': 'Nothing happens at all.',
                'rating': 0
            }
        }
    )
    logger.info(response)


@InsertFuncLog(logger=logger)
def readdb(resource):
    table = resource.Table(TABLENAME)
    response = table.get_item(
        Key={
            # 'sensorId': '2015',
            'CreatedId': '2015'
            # 'getDataTime': '2022/02/16T20:41:31+0900'
        }
    )
    logger.info(response)
