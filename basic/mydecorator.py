import logging
import sys
from functools import wraps
from basic.mylogging_helper import createDeveloplogger
"""[summary]

Returns
-------
[type]
    [description]
"""

logger = createDeveloplogger(__name__, 'log/debug.log')

def uppercase(func):
    def _wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return _wrapper

@uppercase
def greet():
    return 'hello'


def sample1():
    logger.info(greet)
    logger.info(uppercase(greet))
    logger.info('-----')
    logger.info(greet())
    logger.info(uppercase(greet)())


if __name__ == '__main__':
    logger.debug('サンプル')

    sample1()
