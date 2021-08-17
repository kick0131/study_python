import re


def parse_dataapi_result():
    domain = 'http://XXXX'
    api = '.*'
    text = 'abcde'
    pattern = '^'+domain+api+'$'
    regex = re.compile(pattern)
    if regex.match(text) is not None:
        return True
    return False


def change_astar():
    """アスタリスクを置換する
    """
    test = '*ab*cd*'
    return test.replace('*', '')


def change_astar2():
    """アスタリスクを置換する
    """
    test = 'abcde*'
    return test[len(test)-1:]


def re_search():
    """正規表現チェック
    """
    test = 'aaa@xxx.com, bbb@yyy.com, ccc@zzz.net'
    # どちらでもOK
    m = re.search(r'[a-z]+@[a-z]+\.net', test)
    m = re.search(r'\w+@\w+\.net', test)
    print(f'{m}')

    test = 'ABCDE2021.08'
    # どちらでもOK
    m = re.search(r'.*[0-9]{4}\.[0-9]{2}', test)
    m = re.search(r'.*\d{4}\.\d{2}', test)
    print(f'{m}')


if __name__ == '__main__':
    print(f'{re_search()}')
