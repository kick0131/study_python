import logging
import logging.handlers
from logging import DEBUG
from basic.fileAccessSample import createDir

# ハンドラ共通フォーマット
COMMON_HANDLER_FORMAT = '%(asctime)s - %(levelname)s - [%(name)s:%(lineno)s] %(message)s'


def createDeveloplogger(loggername: str, logfilePath: str):
    """開発用ロガーを返す
    """
    logger = logging.getLogger(loggername)
    logger.setLevel(DEBUG)
    # ルートロガーの出力を抑止
    logger.propagate = False
    # ハンドラの登録
    logger.addHandler(createStreamHandler(DEBUG))
    logger.addHandler(createTimedRotatingFileHandler(DEBUG, logfilePath))
    return logger


def createStreamHandler(loglevel: int):
    """標準出力を行うハンドラを返す
    """
    handler = logging.StreamHandler()
    handler.setLevel(loglevel)

    # create formatter
    handler.setFormatter(logging.Formatter(COMMON_HANDLER_FORMAT))

    return handler


def createTimedRotatingFileHandler(loglevel: int, logfilePath: str):
    """ファイル出力を行うハンドラを返す

    ファイル数はbackupCountで定義され、古いものから順に削除する
    """

    # ログディレクトリ生成
    createDir(logfilePath)

    handler = logging.handlers.TimedRotatingFileHandler(
        logfilePath, when='D', interval=1, backupCount=10, encoding='utf-8', delay=False, utc=False, atTime=None)
    handler.setLevel(loglevel)

    # create formatter
    handler.setFormatter(logging.Formatter(COMMON_HANDLER_FORMAT))

    return handler


if __name__ == '__main__':

    logger = createDeveloplogger(__name__, 'log/debug.log')
    logger.info('サンプル')
