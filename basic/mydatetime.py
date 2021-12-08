from datetime import datetime, timezone, timedelta, tzinfo
import time
from basic.logutil.logutil import LogUtil
from dateutil.relativedelta import relativedelta

logger = LogUtil.getlogger(__name__)

"""

    datetime
    コンストラクタにtzinfoを渡すかどうかで内容が変わる
    - Timezone情報を持つモジュール    : aware
    - Timezone情報を持たないモジュール : native

    常にawareを使えばトラブルは少なく済む

    DST
      夏時間の事、基本使わない
"""


# timezoneオブジェクト
# timedelta(0)はName='UTC'が入る、以下は同じ
UTC = timezone(timedelta(0))
UTC = timezone.utc
# JST
JST = timezone(timedelta(hours=+9), 'JST')
# 以下を使いたい場合はpytz.datetimeが必要
# JST = timezone('Asia/Tokyo')


@LogUtil.insertfunclog
def epoctime(dt: datetime) -> float:
    """エポック時間(Unix時刻)の出力

    Parameters
    ----------
    dt : datetime
        [description]

    Returns
    -------
    float
        [description]
    """

    # timetuple()は名前付きタプルを持ったオブジェクトを返す
    # インデックス 属性
    # 0           tm_year
    # 1           tm_mon
    # 2           tm_mday
    # 3           tm_hour
    # ...
    # mktime()はローカル時刻を秒単位で返す
    # マイクロ秒はmicrosecond属性から小数点以下を算出して加える
    epoc = int(time.mktime(dt.timetuple())) + dt.microsecond / 1000000
    logger.info(f'datetime   : {dt}')
    logger.info(f'microsecond: {dt.microsecond}')
    logger.info(f'epoctime   : {epoc}')

    return epoc


@LogUtil.insertfunclog
def epoctext_to_pcapformat(epoctext: str, tz_info: tzinfo = None):
    """
    文字列のエポック時間をpcapのframe.time相当の
    Human Readableなフォーマットに変換

    "1633137008.525944000"
    ↓
    "Oct  2, 2021 10:10:08.525944000 JST"
    """
    f_epoc = float(epoctext)
    logger.info(f'f_epoc   : {f_epoc}')
    epoc_to_pcapformat(f_epoc, tzinfo)
    readable_format = '%b %d, %Y %H:%M:%S.%f000 %Z'
    logger.info(
        f'{datetime.fromtimestamp(f_epoc, tz_info).strftime(readable_format)}')


@LogUtil.insertfunclog
def epoc_to_datetime(epoc: float, tz_info: tzinfo = None):
    """エポック時間からdatetime型に変換

    Parameters
    ----------
    epoc : float
        [description]
    tz_info : tzinfo, optional
        [description], by default None

    Returns
    -------
    [type]
        [description]
    """

    dt_epoc = datetime.fromtimestamp(epoc, tz_info)
    dt_epoc_utc = datetime.fromtimestamp(epoc, UTC)
    dt_epoc_jst = datetime.fromtimestamp(epoc, JST)

    logger.info(f'dt_epoc     : {dt_epoc}')
    logger.info(f'dt_epoc_utc : {dt_epoc_utc}')
    logger.info(f'dt_epoc_jst : {dt_epoc_jst}')

    return dt_epoc


@LogUtil.insertfunclog
def howtimedelta():
    """timedeltaの使い方
    """

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
    """timedelta色々
    """

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

    logger.info('-------------------------------')
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
    """フォーマット色々

    書式指定
    https://docs.python.org/ja/3/library/datetime.html#strftime-and-strptime-behavior

    結論から書くと、タイムゾーンの有無によって
    %zに時差情報が入るかどうかの違いが生じた

    Parameters
    ----------
    dt : datetime
        [description]
    """

    # ElasticSearchで使用されるtimestampフォーマット
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

    # Human Readableな日付表示
    # pcapのframe.timeのフォーマットは以下
    # "Nov 18, 2021 16:37:24.988958000 JST",
    #
    # https://docs.python.org/ja/3/library/datetime.html#strftime-strptime-behavior
    # %b 月名の短縮形
    # %d 0サプレスした日にち
    # %Y 西暦の10進表記
    # %H 24時間表記の時
    # %M 0サプレスした分
    # %S 0サプレスした秒
    # %f マイクロ秒
    # %Z タイムゾーンの略字文字列
    readable_format = '%b %d, %Y %H:%M:%S.%f000 %Z'
    logger.info(f'{datetime.now(UTC).strftime(readable_format)}')


@LogUtil.insertfunclog
def epoc_to_pcapformat(epoc: float, tz_info: tzinfo = None):
    """エポック秒からpcapの文字列時刻表記形式に変換

    Parameters
    ----------
    epoc : float
        エポック秒
    """
    readable_format = '%b %d, %Y %H:%M:%S.%f000 %Z'
    logger.info(
        f'{datetime.fromtimestamp(epoc, tz_info).strftime(readable_format)}')


def formatdatetime(dt: datetime):
    ElasticSearchFmt = '%Y-%m-%dT%H:%M:%S%z'
    return dt.strftime(ElasticSearchFmt)


@LogUtil.insertfunclog
def timestamps():
    pass


if __name__ == '__main__':
    # epoctime(datetime.now())
    # howtimedelta()
    # howtimedelta2()
    # formatdatetimeSample(datetime.now())
    # epoctime(epoc_to_datetime(epoctime(datetime.now(JST)), JST))
    # epoc_to_pcapformat(epoctime(datetime.now()))

    epoctext_to_epoc('1633137008.525944000', UTC)
