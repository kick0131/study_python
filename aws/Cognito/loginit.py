import logging
from logging import DEBUG, INFO, WARN, ERROR, CRITICAL


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
