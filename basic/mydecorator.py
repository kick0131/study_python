import functools
from basic.logutil.mylogging_helper import createDeveloplogger
"""デコレータ色々

Returns
-------
[type]
    [description]
"""

logger = createDeveloplogger(__name__, 'log/debug.log')


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
        logger.info(f'=== {func.__name__} start')
        result = func(*args, **kwargs)
        logger.info(f'=== {func.__name__} end')
        return result
    return _wrapper


def uppercase(func):
    """戻り値を大文字に変換するデコレータ

    Parameters
    ----------
    func : [type]
        デコレータ対象のメソッド
    """
    def _wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        modified_result = original_result.upper()
        return modified_result
    return _wrapper


def first(func):
    """デコレータの呼び出し順序確認
    """
    def _wrapper(*args, **kwargs):
        print('--first--')
        return func(*args, **kwargs)
    return _wrapper


def second(func):
    """デコレータの呼び出し順序確認
    """
    def _wrapper(*args, **kwargs):
        print('--second--')
        return func(*args, **kwargs)
    return _wrapper


class MyDecoSample:
    def __init__(self):
        return None

    def __repr__(self):
        return f'{self.__class__.__name__} {__name__}'

    @InsertFuncLog
    @uppercase
    def sample01(self):
        return 'hello'

    @first
    @second
    def sample02(self, value: str):
        return 'hello' + value


def sample1():
    my = MyDecoSample()
    logger.info(my)
    logger.info(my.sample01())


def sample2():
    my = MyDecoSample()
    logger.info(f'result : {my.sample02("call sample")}')


if __name__ == '__main__':
    sample2()
