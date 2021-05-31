import sys
import os
import pprint
from basic.logutil.mylogging_helper import createDeveloplogger

# ロガー
logger = createDeveloplogger(__name__, 'log/debug.log')


def debuginfo():
    """カレントディレクトリと環境変数PYTHONPATH、エンコーディングの値を表示
    """
    logger.info(os.getcwd())
    logger.info(pprint.pformat(sys.path))
    logger.info(sys.getdefaultencoding())


if __name__ == '__main__':
    debuginfo()

    try:
        logger.debug('テスト')

    except Exception as err:
        logger.error('エラー発生:{}'.format(err))

    pprint.pprint('--- main end ---')
