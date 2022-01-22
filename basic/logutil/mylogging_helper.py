import logging
import logging.handlers
from logging import DEBUG
import functools
from basic.myfileaccess import createDir

# ハンドラ共通フォーマット
COMMON_HANDLER_FORMAT = (
    '%(asctime)s [%(levelname)s] '
    '%(filename)s:%(lineno)s %(funcName)s:%(message)s'
)


def InsertFuncLog(**kwargs):
    """メソッドの開始と終わりのログを付与するデコレータ

        位置引数でロガーを指定した場合のみ動作する

    Returns:
        func: デコレートされたメソッド

    .. code-block:: python

        mylogger=createDeveloplogger

        @InsertFuncLog(logger=mylogger)
        def hoge():
            pass

    """
    logger = kwargs['logger'] if 'logger' in kwargs else None

    def _InsertFuncLog(func):
        """デコレータ本体
        Args:
            func: デコレータ対象のメソッド

        Returns:
            func: デコレートされたメソッド
        """
        funcname = func.__name__

        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            if logger is not None:
                logger.info(f'=== {funcname} start')
            # print(f'args:{args} kwargs:{kwargs}')
            result = func(*args, **kwargs)
            if logger is not None:
                logger.info(f'=== {funcname} end')
            return result
        return _wrapper
    return _InsertFuncLog


def createDeveloplogger(
        loggername: str, logfilePath: str, loglevel: int = DEBUG):
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
    # logger.propagate = False
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
        logfilePath, when='D', interval=1, backupCount=10,
        encoding='utf-8', delay=False, utc=False, atTime=None)
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
