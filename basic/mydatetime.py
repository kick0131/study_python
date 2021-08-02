from datetime import datetime, timezone, timedelta
import time
from basic.logutil.logutil import LogUtil
from dateutil.relativedelta import relativedelta

logger = LogUtil.getlogger(__name__)

'''
Timezone情報を持つモジュール    : aware
Timezone情報を持たないモジュール : native
'''

# timezoneオブジェクト
JST = timezone(timedelta(hours=+9), 'JST')


@LogUtil.insertfunclog
def epoctime(dt: datetime):
    '''
    エポック時間(Unix時刻)の出力
    '''
    logger.info(f'datetime: {dt}')

    epoc = int(time.mktime(dt.timetuple()))
    logger.info(f'epoctime: {epoc}')


@LogUtil.insertfunclog
def howtimedelta():
    '''
    timedeltaの使い方
    '''
    # 時間の間隔を表すtimedeltaオブジェクト
    delta1 = timedelta(seconds=10)
    logger.info(f'delta: {delta1}')

    # datetime型に加算が可能
    now = datetime.now()
    now2 = now + delta1
    logger.info(f'now      : {now}')
    logger.info(f'add delta: {now2}')


@LogUtil.insertfunclog
def howtimedelta2():
    '''
    timedelta色々
    - 閏年
    '''

    # 閏年の境目をサンプルデータとして用意
    dt = datetime.now(JST)
    # dt = datetime(2001, 2, 28, tzinfo=JST)

    logger.info(f'dt : {dt}')

    # -------------------------------------------
    # キリの良い時間の算出
    # -------------------------------------------
    # 特定日の６時
    set_quarter = relativedelta(hour=6, minute=0, second=0, microsecond=0)
    dt = dt + set_quarter
    logger.info(f'1/4 day : {dt}')
    # 特定日の１２時
    add_quarter = timedelta(hours=6)
    dt = dt + add_quarter
    logger.info(f'2/4 day : {dt}')
    dt = dt + add_quarter
    logger.info(f'3/4 day : {dt}')
    dt = dt + add_quarter
    logger.info(f'4/4 day : {dt}')

    logger.info(f'-------------------------------')
    # -------------------------------------------
    # 時間をずらす
    # -------------------------------------------
    # 翌日
    add1d = timedelta(days=1)
    logger.info(f'+1d: {formatdatetime(dt + add1d)}')
    # 翌月
    add1m = relativedelta(months=1)
    logger.info(f'+1m: {formatdatetime(dt + add1m)}')
    # 翌年
    add1y = relativedelta(years=1)
    logger.info(f'+1y: {formatdatetime(dt + add1y)}')
    # 前日
    minus1d = timedelta(days=-1)
    logger.info(f'-1d: {formatdatetime(dt + minus1d)}')
    # 先月
    minus1m = relativedelta(months=-1)
    logger.info(f'-1m: {formatdatetime(dt + minus1m)}')
    # 去年
    minus1y = relativedelta(years=-1)
    logger.info(f'-1y: {formatdatetime(dt + minus1y)}')


@LogUtil.insertfunclog
def formatdatetimeSample(dt: datetime):
    '''
    書式指定
    https://docs.python.org/ja/3/library/datetime.html#strftime-and-strptime-behavior
    '''

    # 2020-10-01T00:00:00+09:00
    ElasticSearchFmt = '%Y-%m-%dT%H:%M:%S%z'

    # 初期値
    logger.info(f'before        : {dt}')

    # Timezone指定なし
    newdt = dt.strftime(ElasticSearchFmt)
    logger.info(f'after(not tz) : {newdt}')

    # Timezone指定あり
    newdt = datetime.fromtimestamp(dt.timestamp(), JST)
    newdt = newdt.strftime(ElasticSearchFmt)
    logger.info(f'after(use tz) : {newdt}')


def formatdatetime(dt: datetime):
    ElasticSearchFmt = '%Y-%m-%dT%H:%M:%S%z'
    return dt.strftime(ElasticSearchFmt)


@LogUtil.insertfunclog
def timestamps():
    pass


if __name__ == '__main__':
    # epoctime(datetime.now())
    # howtimedelta()
    howtimedelta2()
    # formatdatetime(datetime.now())
