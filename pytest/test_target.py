import platform


CONST_VALUE = 'this is const'


def get_platform():
    return platform.system()


if __name__ == '__main__':
    print(f'{get_platform()}')
