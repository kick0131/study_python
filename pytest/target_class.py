"""pytest動作確認用
"""
import loginit

logger = loginit.uselogger(__name__)


def funcname(func):
    """デコレータを使った関数ログ
    """
    def _wrapper(*args, **kwargs):
        print(f'=== {func.__name__} start')
        result = func(*args, **kwargs)
        print(f'=== {func.__name__} end')
        return result
    return _wrapper


class BaseClass:
    @funcname
    def basefunc01(self):
        print('test method called')
        return 'ABC'


if __name__ == '__main__':
    target = BaseClass()
    print(f'test method result : {target.basefunc01()}')
