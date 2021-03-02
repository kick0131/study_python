import functools
from basic.mylogging_helper import createDeveloplogger
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
    def _wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return _wrapper


class MyDecoSample:
    def __init__(self):
        return None

    def __repr__(self):
        return f'{self.__class__.__name__} {__name__}'

    @InsertFuncLog
    def sample01(self):
        return 'hello'

    def sample02(self, value: str):
        return 'hello' + str


@uppercase
def greet():
    return 'hello'


def sample1():
    logger.info(greet)
    logger.info(uppercase(greet))
    logger.info('-----')
    logger.info(greet())
    logger.info(uppercase(greet)())


def sample2():
    my = MyDecoSample()
    logger.info(my)
    logger.info(my.sample01())


if __name__ == '__main__':
    sample2()
