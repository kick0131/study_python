import base64
import json
from basic.logutil.mylogging_helper import createDeveloplogger, InsertFuncLog

logger = createDeveloplogger(__name__, 'log/debug.log')

"""base64モジュールの使い方

    == 基本
    文字列からバイト型への変換
    str.encode()

    バイト型から文字列への変換
    byte.decode()

"""


@InsertFuncLog(logger=logger)
def b64encode(message: str):
    bytedata = message.encode()
    logger.info('--- base64encode ---')
    logger.info(f'normal : {base64.b64encode(bytedata)}')
    logger.info(f'urlsafe: {base64.urlsafe_b64encode(bytedata)}')
    return base64.b64encode(bytedata)


@InsertFuncLog(logger=logger)
def b64decode(bytedata: bytes):
    logger.info('--- base64decode ---')
    logger.info(f'normal : {base64.b64decode(bytedata)}')
    logger.info(f'urlsafe: {base64.urlsafe_b64decode(bytedata)}')


@InsertFuncLog(logger=logger)
def jsonencode():
    context = {
        "key": "value",
        "numParam": 123,
        "boolParam": True
    }

    # base64化
    b64_info = base64.b64encode(json.dumps(context).encode('utf8'))
    logger.info(f'b64_info   : {b64_info} type: {type(b64_info)}')
    # byte -> str
    # 注意！！末尾にカンマがあるとtuple扱いになる
    # b64_decode = b64_info.decode('utf8'),
    b64_decode = b64_info.decode('utf8')
    logger.info(f'b64_decode : {b64_decode} type: {type(b64_decode)}')


if __name__ == '__main__':
    encoded = b64encode('abcde')
    b64decode(encoded)
    jsonencode()


