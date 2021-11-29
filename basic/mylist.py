import json

def xxx():
    listdata = [
        ['aaa', 123, True],
        ['bbb', 456, False],
    ]
    strdatas = (x[0] for x in listdata)
    intdatas = (x[1] for x in listdata)
    for strdata, intdata in zip(strdatas, intdatas):
        print(f'strdata:{strdata} intdata:{intdata}')


def stringlist():
    """文字列化したリストを扱うパターン
    """
    listdata = '[{"greet":"hello","os":"linux"},{"greet":"こんにちは","os":"windows"}]'
    output = json.loads(listdata)
    print(output)


if __name__ == '__main__':
    stringlist()
