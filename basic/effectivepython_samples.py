import functools
from basic.mylogging_helper import createDeveloplogger

# ロガー
logger = createDeveloplogger(__name__, 'log/debug.log')


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.debug(f'{func.__name__}({args}, {kwargs}) -> {result}')
        return result
    return wrapper


class EffectivePythonSample():
    """EffectivePythonSample class
    """

    def __init__(self, message):
        logger.debug('message')

    @trace
    def fibonacci(self, n):
        """フィボナッチ数列を返却
        """
        if n in (0, 1):
            return n
        return (self.fibonacci(n - 2) + self.fibonacci(n - 1))


def arg_and_kwarg(*args, **kwargs):
    logger.info(f'args:{args} kwargs:{kwargs}')


if __name__ == '__main__':
    logger.info('=== EffectivePythonSample')
    target = EffectivePythonSample('hoge')
    logger.info('-------------------------')
    target.fibonacci(3)
    logger.info('-------------------------')
    arg_and_kwarg('adam', 15, {'addr': 'tokyo'}, param='aaa', dummy='bbb')
