import functools
from loggingHelper import createDeveloplogger

# ロガー
logger = createDeveloplogger(__name__, 'log/debug.log')


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.debug(f'{func.__name__}({args}, {kwargs}) -> {result}')
        return result
    return wrapper

@trace
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n-1))


class EffectivePythonSample():
    """EffectivePythonSample class
    """

    def __init__(self, message):
        logger.debug(f'message')

    # def trace(self, func):
    #     def wrapper(self, *args, **kwargs):
    #         result = self.func(*args, **kwargs)
    #         logger.debug(f'{self.func.__name__}({args}, {kwargs}) -> {result}')
    #         return result
    #     return wrapper

    @trace
    def fibonacci(self, n):
        """フィボナッチ数列を返却

        概要の通り。テストコード

        Args:
            階層の深さ

        Returns:
            フィボナッチ数列の総和

        Note:
            途中結果はtraceで出力
        """
        if n in (0, 1):
            return n
        return (self.fibonacci(n - 2) + self.fibonacci(n-1))


if __name__ == '__main__':
    logger.info('=== EffectivePythonSample')
    target = EffectivePythonSample('hoge')
    target.fibonacci(3)
    logger.info(f'=== {target.fibonacci}')

