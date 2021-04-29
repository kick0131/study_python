"""propagateの挙動確認サンプル

1. ログレコード生成
2. ロガーがログレコードをハンドラへ送信
3. ハンドラでログレコードを処理

"""
import logging

LOGFORMAT = '%(asctime)s [%(levelname)s] %(message)s'


def checker(func):
    """チェック用デコレータ

    ロガー返却メソッドにデコレートし、動作確認処理を行います

    - 繰り返しロガー生成

    """
    def _wrapper():
        for _ in range(3):
            print('-----------------------')
            logger = func()
            logger.debug('hello world')
            logger.info('hello world')
            logger.warning('hello world')
            logger.error('hello world')
        return logger
    return _wrapper


@checker
def getlogger():
    """ロガー取得

    最もシンプルなロガー
    デフォルトのエラーレベルはWARN
    このロガーは**ログフォーマットもハンドラも変えられない**

    """
    _logger = logging.getLogger(__name__)
    return _logger


# @checker
def getlogger_top():
    """ロガー取得

    公式のサンプルほぼそのまま
    欠点はこのメソッドが複数回呼ばれるとログが重複してしまう

    """
    # create logger
    logger = logging.getLogger('top')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter(LOGFORMAT)

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    return logger


# @checker
def getlogger_topsub1():
    """ロガー取得

    topを親に持つ

    """
    logger = logging.getLogger('top.sub1')
    logger.setLevel(logging.DEBUG)
    # ⭐️親(Top)のハンドラを継承するかどうか
    logger.propagate = False

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter(LOGFORMAT)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger


# @checker
def getlogger_topsub2():
    """ロガー取得

    topを親に持つ

    """
    logger = logging.getLogger('top.sub2')
    logger.setLevel(logging.DEBUG)
    # ⭐️親(Top)のハンドラを継承するかどうか
    logger.propagate = True

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter(LOGFORMAT)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger


if __name__ == '__main__':
    # デコレータ内で処理を実行
    logger = getlogger()
    logger.info('=== sample ===')
