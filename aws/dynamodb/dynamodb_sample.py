# from botocore.exceptions import ClientError
from basic.logutil.mylogging_helper import InsertFuncLog, createDeveloplogger
import aws.myenv as myenv

TABLENAME = myenv.DYNAMODB_TABLE
logger = createDeveloplogger(__name__, 'log/debug.log')


@InsertFuncLog(logger=logger)
def writedb(resource, item):
    table = resource.Table(TABLENAME)
    response = table.put_item(Item=item)
    logger.info(response)


@InsertFuncLog(logger=logger)
def readdb(resource, key):
    table = resource.Table(TABLENAME)
    response = table.get_item(Key=key)
    logger.info(response)


# 重複を許可する際に設定するキー
PKEY = 'CreatedId'


@InsertFuncLog(logger=logger)
def bulkinsert(resource, listitem):
    table = resource.Table(TABLENAME)
    with table.batch_writer(overwrite_by_pkeys=[PKEY]) as batch:
        for data in listitem:
            batch.put_item(Item=data)
