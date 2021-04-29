"""pytest動作確認用
"""
import loginit
import sys

logger = loginit.uselogger(__name__)


def funcname():
    return f'{sys._getframe().f_code.co_name}'


class BaseClass:
    def basefunc01(self):
        # logger.info(f'{sys._getframe().f_code.co_name}')
        logger.info(f'{funcname}')


if __name__ == '__main__':
    target = BaseClass()
    target.basefunc01()
