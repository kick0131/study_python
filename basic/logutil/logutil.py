import logging
from logging import DEBUG, INFO, WARN, ERROR, CRITICAL
import functools
import os

#: デフォルトログレベル
DEFAULT_LOGLEVEL = INFO

#: ログフォーマット_詳細
LOGUTIL_LOGFORMAT_A = (
    '%(asctime)s [%(levelname)s] %(thread)d '
    '%(pathname)s:%(funcName)s:%(lineno)s %(message)s'
)

#: ログフォーマット_シンプル
LOGUTIL_LOGFORMAT_B = (
    '%(asctime)s [%(levelname)s] '
    '%(filename)s:%(lineno)s %(funcName)s:%(message)s'
)


def str_to_loglevel(logstr: str):
    """ログレベル文字列をloggingのログレベルに変換する

    以下の変換に対応,対応する文字列がなかった場合、定数DEFAULT_LOGLEVELを返却する

    * DEBUG
    * INFO
    * WARN
    * ERROR
    * CRITICAL

    .. code-block:: python

        loglevel = str_to_loglevel('INFO')

    Args:
        logstr (str): ログレベル文字列

    Returns:
        int: loggingモジュールのログレベル定数
    """
    # 引数チェック
    if logstr is None or len(logstr) == 0:
        return DEFAULT_LOGLEVEL

    ulogstr = logstr.upper()

    # LOGLEVEL変換
    if 'DEBUG' == ulogstr:
        return DEBUG
    if 'INFO' == ulogstr:
        return INFO
    if 'WARN' == ulogstr:
        return WARN
    if 'ERROR' == ulogstr:
        return ERROR
    if 'CRITICAL' == ulogstr:
        return CRITICAL
    return DEFAULT_LOGLEVEL


class LogUtil:
    """**クラス説明**

    ログ出力機能を提供します
    """
    # ロガー
    _innerlogger = None

    def __init__(self):
        """**コンストラクタ**

        特に使いません、getLoggerを使用してください

        """
        pass

    def __repr__(self):
        return 'LogUtil()'

    @classmethod
    def insertfunclog(cls, func: object):
        """開始終了の自動ログ出力デコレータ

        メソッドの開始と終了時のログ出力を行う

        .. code-block:: python

            @insertfunclog
            def dummy():
                pass

        .. warning::

            内部でロガーを使用しているため、getLoggerでロガーが生成されている必要があります。
            未使用の場合、開始終了ログは出力されません。

        Args:
            func: デコレータ付与対象のメソッド

        Returns:
            object: 元のオブジェクトに開始終了ログが付与されたメソッドオブジェクト
        """
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            funcname = func.__name__
            if cls._innerlogger is not None:
                cls._innerlogger.info(f'=== {funcname} start')
            result = func(*args, **kwargs)
            if cls._innerlogger is not None:
                cls._innerlogger.info(f'=== {funcname} end')
            return result
        return _wrapper

    @classmethod
    def getlogger(cls, modulename: str):
        """ロガーを返却する

        .. code-block:: python

            from dcpfutils.logutil import LogUtil
            logger = LogUtil.getlogger(__name__)
            logger.info('hello')

        .. note::

            環境変数LOGLEVELが定義されていた場合、
            取得した文字列をログレベルと判断し、変換処理を行います。
            環境変数が取得できなかったときのデフォルト値はINFOです。

        Args:
            modulename (str): ログ出力時の名称、モジュール名を期待

        Returns:
            object: loggerオブジェクト
        """
        if cls._innerlogger is not None:
            return cls._innerlogger

        # get loglevel from environment
        loglevel = str_to_loglevel(
            os.getenv("LOGLEVEL", default=''))

        # create logger
        logger = logging.getLogger(modulename)
        logger.propagate = False

        # set handler
        handler = logging.StreamHandler()
        handler.setLevel(loglevel)

        # create formatter
        formatter = logging.Formatter(LOGUTIL_LOGFORMAT_B)
        handler.setFormatter(formatter)

        # add handler to root logger
        logger.addHandler(handler)
        logger.setLevel(DEBUG)

        cls._innerlogger = logger
        return cls._innerlogger


@LogUtil.insertfunclog
def testcode():
    """ローカル実行用のテストメソッド
    """
    logger.debug(f'==={__name__} sample')
    logger.info(f'==={__name__} sample')
    logger.warning(f'==={__name__} sample')
    logger.error(f'==={__name__} sample')


def exception_sample():
    """logger.exceptionの使い方
    """
    try:
        raisesample()
    except(Exception):
        logger.exception('ログ＋スタックトレースログ、例外スコープ内で使う')


def raisesample():
    raise Exception('サンプル例外')


if __name__ == '__main__':
    logger = LogUtil.getlogger(__name__)
    testcode()
    exception_sample()
