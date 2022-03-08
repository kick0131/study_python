"""バリデーション色々
"""


def typecheck():
    """型判定
    """
    for data in ['moji', 12345, {'key': 'value'}]:
        if type(data) is str:
            print(f'{data} is str')
        elif type(data) is dict:
            print(f'{data} is dict')
        else:
            print(f'{data} is not str')


if __name__ == '__main__':
    typecheck()
