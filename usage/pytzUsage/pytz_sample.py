from datetime import datetime
from pytz import timezone
import pytz

# 自作パッケージ
from basic.logutil.logutil import LogUtil

logger = LogUtil.getlogger(__name__)


@LogUtil.insertfunclog
def init():
    # Timezone UTC
    utc = pytz.utc
    logger.info(f'utc      :{utc}')
    logger.info(f'utc.zone :{utc.zone}')
    # Timezone JST
    jst = timezone('Asia/Tokyo')
    logger.info(f'jst      :{jst}')
    logger.info(f'jst.zone :{jst.zone}')

    return utc, jst


def sampledatetime(utc, jst):
    # Datetime
    utc_dt = utc.localize(datetime(2020, 2, 28, 23, 59, 59))
    jst_dt = jst.localize(datetime(2020, 2, 28, 23, 59, 59))
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    logger.info(f'utc      :{utc_dt.strftime(fmt)}')
    logger.info(f'jst      :{jst_dt.strftime(fmt)}')


if __name__ == '__main__':
    utc, jst = init()
    sampledatetime(utc, jst)
