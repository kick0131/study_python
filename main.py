import sys
import os
import pprint
from basic.loggingHelper import createDeveloplogger
# import aws.Cognito.cognitoMain
# import basic.datatype

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
        # Cognito.cognitoMain.lambda_handler('', '')

    except Exception as err:
        logger.error('エラー発生:{}'.format(err))

    pprint.pprint('--- main end ---')
