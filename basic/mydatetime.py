import datetime
import time
import sys
import mylogging_helper

logger = mylogging_helper.createDeveloplogger(__name__, 'log/debug.log')


def epoctime(dt: datetime):
    logger.info(f'datetime: {dt}')

    epoc = int(time.mktime(dt.timetuple()))
    logger.info(f'epoctime: {epoc}')


def epoctime_plus(dt: datetime, delta: datetime.timedelta):
    logger.info(f'datetime: {dt}')

    epoc = int(time.mktime(dt.timetuple()))
    logger.info(f'epoctime: {epoc}')


def howtimedelta():
    # 時間の間隔を表すtimedeltaオブジェクト
    delta1 = datetime.timedelta(seconds=10)
    logger.info(f'delta: {delta1}')

    # datetime型に加算が可能
    now = datetime.datetime.now()
    now2 = now + delta1
    logger.info(f'now      : {now}')
    logger.info(f'add delta: {now2}')


if __name__ == '__main__':
    epoctime(datetime.datetime.now())
    howtimedelta()
