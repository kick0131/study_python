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



if __name__ == '__main__':
    print(f'{change_astar2()}')


