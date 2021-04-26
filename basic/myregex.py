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


if __name__ == '__main__':
    print(f'{parse_dataapi_result()}')
