import platform

'''試験対象

pymockから内容を書き換える事を確認する為のサンプルクラス、モジュール

'''

CONST_VALUE = 'this is const'


def get_platform():
    return platform.system()


def funcname(func):
    """デコレータを使った関数ログ
    """
    funcname = func.__name__

    def _wrapper(*args, **kwargs):
        print(f'=== {funcname} start')
        result = func(*args, **kwargs)
        print(f'=== {funcname} end')
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
    print(f'{get_platform()}')
