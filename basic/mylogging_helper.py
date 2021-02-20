import logging
import logging.handlers
from functools import wraps
from logging import DEBUG, INFO, WARN
from basic.myfileaccess import createDir

# ハンドラ共通フォーマット
COMMON_HANDLER_FORMAT = '%(asctime)s - %(levelname)s - [%(name)s:%(lineno)s] %(message)s'

def loglevel(level: int):
    """ログレベルを変更するデコレータ

    Parameters
    ----------
    level : int
        ログレベル
    """
    def _loglevel(func):
        @wraps(func)
        def inner(*arg, **kwarg):
            # get logger and change logLevel
            ret = func(*arg, **kwarg)
            ret.setLevel(level)
            return ret
        return inner
    return _loglevel


def createDeveloplogger(loggername: str, logfilePath: str, loglevel: int = DEBUG):
    """開発用ロガーを返す

    ログレベルはデフォルト引数を取り、デバッグレベルとする

    Parameters
    ----------
    loggername : str
        ロガー名
    logfilePath : str
        ログ出力先
    loglevel : int, optional
        ログレベル, by default DEBUG

    Returns
    -------
    [type]
        [description]
    """
    logger = logging.getLogger(loggername)
    logger.setLevel(loglevel)
    # ルートロガーの出力を抑止
    logger.propagate = False
    # ハンドラの登録
    logger.addHandler(createStreamHandler(loglevel))
    logger.addHandler(createTimedRotatingFileHandler(DEBUG, logfilePath))
    return logger
    

def createStreamHandler(loglevel: int):
    """標準出力を行うハンドラを返す

    Parameters
    ----------
    loglevel : int
        ログレベル

    Returns
    -------
    [type]
        [description]
    """
    handler = logging.StreamHandler()
    handler.setLevel(loglevel)

    # create formatter
    handler.setFormatter(logging.Formatter(COMMON_HANDLER_FORMAT))

    return handler


def createTimedRotatingFileHandler(loglevel: int, logfilePath: str):
    """ファイル出力を行うハンドラを返す

    ファイル数はbackupCountで定義され、古いものから順に削除する

    Parameters
    ----------
    loglevel : int
        ログレベル
    logfilePath : str
        ログ出力先

    Returns
    -------
    [type]
        [description]
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
    logger.debug('サンプル')
    logger.info('サンプル')
    logger.warning('サンプル')
    logger.error('サンプル')
