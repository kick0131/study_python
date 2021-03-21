import logging
from logging import DEBUG
import functools


def InsertFuncLog(func):
    """メソッドの開始と終わりのログを付与するデコレータ

    Parameters
    ----------
    func : function
        デコレータ対象のメソッド

    Returns
    -------
    function
        デコレートされたメソッド
    """
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        # 位置引数でロガーが定義されているかチェック
        logger = kwargs['logger'] if 'logger' in kwargs else None
        if logger is not None:
            logger.info(f'=== {func.__name__} start')
        print(f'args:{args} kwargs:{kwargs}')
        result = func(*args, **kwargs)
        if logger is not None:
            logger.info(f'=== {func.__name__} end')
        return result
    return _wrapper


def uselogger(modulename):
    """ロガー返却処理

    コンソール出力のみ行うシンプルなロガー

    Args
      modulename(str): ロガーを使用するモジュール名

    """

    # create logger
    logger = logging.getLogger(modulename)
    logger.propagate = False

    # set handler
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - [%(name)s:%(lineno)s] %(message)s')
    handler.setFormatter(formatter)

    # add handler to root logger
    logger.addHandler(handler)
    logger.setLevel(DEBUG)

    return logger
