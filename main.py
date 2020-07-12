import sys
import os
from pprint import pformat
from loggingHelper import createDeveloplogger
import Cognito.cognitoMain
import datatype

# 環境変数PYTHONPATHでmain.pyディレクトリまでのパスを通すこと

# ロガー
logger = createDeveloplogger(__name__, 'log/debug.log')


def debuginfo():
    """カレントディレクトリと環境変数PYTHONPATH、エンコーディングの値を表示
    """
    logger.info(os.getcwd())
    logger.info(pformat(sys.path))
    logger.info(sys.getdefaultencoding())


if __name__ == '__main__':
    # debuginfo()

    try:
        logger.debug('テスト')
        # Cognito.cognitoMain.lambda_handler('', '')
        effectivePythonSample()

    except Exception as err:
        logger.error('エラー発生:{}'.format(err))
