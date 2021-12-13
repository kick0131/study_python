import json
import re


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

    # list
    print(f'type:{type(output)} output:{output}')
    # dict
    print(f'type:{type(output[0])} output:{output[0]}')


def listcomprehension():
    """リスト内包処理

    [式 for 任意の変数名 in イテラブルオブジェクト if 条件式]
    -----
    【条件式】に合致した【イテラブルオブジェクト】を【任意の変数名】に出力し、
    【式】で評価したものをリスト化する

    """
    names = ['ada', 'bob', 'adam', 'caccy', 'amanda']
    a_names = [
        name + ' start with A.' for name in names if re.match('a+', name)]
    for name in a_names:
        print(f'{name}')


def listcomprehension2():
    """リスト内包処理2

    元のリストがdict型だった場合

    """
    listdata = '[{"greet":"hello","os":"linux"},{"greet":"こんにちは","os":"windows"}]'
    output = json.loads(listdata)

    dictitems = [dictitem for dictitem in output if re.match(
        'hello', dictitem['greet'])]
    for dictitem in dictitems:
        print(f'{dictitem}')


def appendlistmove():
    """append操作の罠

    オブジェクト要素のコピー例として、
    一時オブジェクトを経由せずに直接appendするのはいけないという話

    """
    listdata = '[{"greet":"hello","os":"linux"},{"greet":"こんにちは","os":"windows"}]'
    output = json.loads(listdata)

    # --------------------------------------------------------
    # OKパターン
    #
    dictlist = []
    for listitem in output:
        tmp_dict = {}
        # オブジェクトIDの確認
        print(id(tmp_dict))
        tmp_dict['greet'] = listitem['greet']
        tmp_dict['os'] = listitem['os']
        dictlist.append(tmp_dict)

    # tmp_dictで格納しているオブジェクトが毎回異なるので
    # 設定元を変えてもコピー先は影響しない
    output[0]['greet'] = 'hogehoge'
    for listitem in dictlist:
        print(listitem)

    # --------------------------------------------------------
    # NGパターン
    # 直接オブジェクトをappendしているのでsharrow copyになっている
    #
    dictlist = []
    for listitem in output:
        dictlist.append(listitem)
    output[0]['greet'] = 'hogehoge'
    for listitem in dictlist:
        print(listitem)


if __name__ == '__main__':
    appendlistmove()
