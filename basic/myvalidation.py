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


def includestr():
    """文字列の部分チェック

    startswith句で部分一致のチェック
    """
    target = '2022/03/08 12:34:56'
    search_str = '2022/03/08 12:34:00'

    # 秒を除いた'2022/03/08 12:34'で部分チェック
    if target.startswith(search_str[:-3]):
        print(f'{search_str} は {target} に含まれる')


if __name__ == '__main__':
    typecheck()
    includestr()
