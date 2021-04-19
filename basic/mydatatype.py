# 各種データ型
# ・リスト
# ・タプル
# ・辞書

import logging
import sys
# import json
import re
from functools import wraps

logging.basicConfig(
    level=logging.DEBUG,            # ログレベル
    format=' %(asctime)s - %(levelname)s - %(message)s')


def printfunc():
    """ 関数名を出力するデコレータ
    """
    def _printfunc(func):
        @wraps(func)
        def inner(*arg, **kwarg):
            # get logger and change logLevel
            ret = func(*arg, **kwarg)
            # ret.setLevel(level)
            return ret
        return inner
    return _printfunc


def listsample():
    """リスト型の動作サンプル

    入れ子の編集、タプルへの変換

    Note:
        基本動作の確認、関数内のコードは都度編集されることを想定。

    """

    logging.debug('=== [{}] start ==='.format(sys._getframe().f_code.co_name))

    # 基本形
    val = [1, 'cat', 3, 'dog']
    for i in range(len(val)):
        print(val[i])

    # 入れ子
    val = [
        [1, 'cat', 3, 'dog'],
        [2, 'lion', 4, 'tiger']
    ]
    print(val)
    for i in range(len(val)):
        for k in range(len(val[i])):
            print(val[i][k])

    # 編集
    val[1][2] = '★★★'
    print(val)

    # 検索
    # loggingモジュールとprintメソッドの出力順に注意
    # print分が出力された後にloggingが出力される
    logging.debug('cat' in val[0])

    # タプルに変換
    val = tuple(val)
    logging.info(type(val))


def listisEmpty():
    """リスト型の空要素を判定

    リスト型の空要素判定コード

    Note:
        コピー用途

    """
    mylist = []
    if not mylist:
        logging.info('None!!')
    else:
        logging.info('Exists!!')


def tuplesample():
    """タプル型の動作サンプル

    入れ子の編集、リスト型への変換

    Note:
        基本動作の確認、関数内のコードは都度編集されることを想定。

    """

    logging.debug('=== [{}] start ==='.format(sys._getframe().f_code.co_name))

    # 基本形
    val = (1, 'cat', 3, 'dog')
    for i in range(len(val)):
        print(val[i])

    # 入れ子
    val = (
        (1, 'cat', 3, 'dog'),
        (2, 'lion', 4, 'tiger')
    )
    print(val)
    for i in range(len(val)):
        for k in range(len(val[i])):
            print(val[i][k])

    # 編集
#    l[1][2] = '★★★'  # NG imutable
#    print(l)

    # 検索
    logging.debug('cat' in val[0])

    # リストに変換
    val = list(val)
    logging.info(type(val))


def dicsample():
    """辞書型の動作サンプル

    入れ子の編集

    Note:
        基本動作の確認、関数内のコードは都度編集されることを想定。

    """

    logging.debug('=== [{}] start ==='.format(sys._getframe().f_code.co_name))

    # 基本形
    # キーが同じものは後勝ちで上書きされる
    val = {'key1': 1, 'key2': 'cat', 'key3': 3, 'key4': 'dog'}
    for i in val.items():
        print(i)

    # 入れ子
    val = {
        'key1': {'key11': 1, 'key12': 'cat', 'key13': 3, 'key14': 'dog'},
        'key2': {'key21': 5, 'key22': 'lion', 'key23': 7, 'key24': 'tiger'}
    }

    # ('key1', {'key11': 1, 'key12': 'cat', 'key13': 3, 'key14': 'dog'})
    #          1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #            2~~~~~~~~  2~~~~~~~~~~~~~  2~~~~~~~~~~  2~~~~~~~~~~~~~
    # 1: 外側のループのvaluesで取得する範囲
    # 2: 内側のループのitemsで取得する範囲
    for i in val.values():
        print(i)
        for k in i.items():
            print(k)

    # 編集
    val['key2']['key22'] = '★★★'
    print(val)

    # 検索
    logging.info('cat' in val['key1'].values())


def listdiccreate():
    """リスト内辞書データの連結作成

    リスト内に辞書型が組合された場合の動作サンプル。
    主にjsonを想定したケース。

    Returns:
        連結された辞書データ

    Note:
        呼び出し元でjsonとして扱う想定
        {
            "data": [
                {"name":"Taro","attr":"Man"},
                {"name":"Hanako","attr":"Woman"},
            ]
        }
    """

    result = {}
    mylist1 = []
    mylist2 = []
    mylist1.append({"name": "Taro", "attr": "Man"})
    mylist2.append({"name": "Hanako", "attr": "Woman"})
    mylist1.extend(mylist2)
    result['data'] = mylist1
    return result


def listdic_extraction():
    """リスト内辞書データの抽出

    リスト内に辞書型が組合されたデータの抽出サンプル。
    DataAPIの応答結果を想定したケース。

    Note:
        以下テストデータとする
        {
            "data": [
                {"name":"Taro","attr":"Man"},
                {"name":"Hanako","attr":"Woman"},
            ]
        }

        Valueのみを抽出し、レコード単位でリストにする
        [["Taro","Man"]["Hanako","Woman"]]

    """
    # 抽出対象
    result = {}
    result['data'] = [{"name": "Taro", "attr": "Man"},
                      {"name": "Hanako", "attr": "Woman"}]

    # 処理ロジック
    newlist = []
    for dicitem in result['data']:
        locallist = []
        for value in dicitem.values():
            locallist.append(value)
        newlist.append(locallist)

    # 取得結果確認
    logging.info(newlist)


def stringsub():
    before1 = ' Bearer XXXX.YYYY.ZZZZ'  # OK
    before2 = 'Bearer XXXX.YYYY.ZZZZ'  # OK
    before3 = ' XXXX.YYYY.ZZZZ'        # NG
    before4 = 'XXXX.YYYY.ZZZZ'         # NG
    before5 = (
        'Bearer eyJraWQiOiJTZ0c1T0xKalpzN2Y3c09JNlpUVStmOGtyTThuOFwvT3BLVE8zMkZUY2EyMD0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0YzUxNDQ0Zi00NGZhLTQ4NmYtYTRiZC0xMzk5ZDcxNzRlMjMiLCJhdWQiOiI1djFkMXVhZDdvYmExOGw2c3A3aDc0N3VxYSIsImV2ZW50X2lkIjoiZThkZTBiZmYtNjhhYS00NTdmLTgwZDAtMmIyMGQ3ZTY1Njg3IiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2MTUyNjg0MjAsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1ub3J0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1ub3J0aGVhc3QtMV9UZmp1SVJGQmEiLCJjb2duaXRvOnVzZXJuYW1lIjoiaGlyYW1hdHN1IiwiZXhwIjoxNjE1MjcyMDIwLCJpYXQiOjE2MTUyNjg0MjAsImVtYWlsIjoiaGlyYW1hdHN1LmNockBuY29udHIuY29tIn0.TwjRTEqDwMoS7euK2j9qA2khCrYwiw3tkGWarkBcOSpXb2ZIyzMY4bLsRBa-z0pHkbuw_BFTUxbiJQIZN78SG7Y7lS0GIJuWcmQPVread10LmJ_3uNKL4IAp6caJEI9DfOvWi99o-AWZVoJXWxWSas538wgLnglyU3ZsfDRyfSfw67n-RwcM4c9RlD4XGuNv6EhG8EdBZr9NUqshU1FjLtMlfPxP4T1b8-gH-VptFS-p9U2rubTynGk1JDvZam4D3OEFxKfYqiia2tczRFjy2_V3HAPehmsz5Q2x2ciki_Bj2I1LjUIaGAJ_qZtr437H4hYFIAQRolViY4GbjCw7sg'
    )
    if 'Bearer' in before1:
        logging.info(f'before1 : {re.sub(".*(Bearer) ", "", before1)}')
    if 'Bearer' in before2:
        logging.info(f'before2 : {re.sub(".*(Bearer) ", "", before2)}')
    if 'Bearer' in before3:
        logging.info(f'before3 : {re.sub(".*(Bearer) ", "", before3)}')
    if 'Bearer' in before4:
        logging.info(f'before4 : {re.sub(".*(Bearer) ", "", before4)}')
    if 'Bearer' in before5:
        logging.info(f'before5 : {re.sub(".*(Bearer) ", "", before5)}')


def buildResponse(resdata: dict):
    """辞書型の内容をJSONとして返す

    # return {
    #     "resCode": resCode,
    #     "resMessage": f'resMessage[{resCode}]',
    #     "resData": resdata
    # }

    Parameters
    ----------
    resdata : dict
        オーソライザの戻り値として渡す情報

    Returns
    -------
    dict
        json形式の戻り値情報
    """
    return {k: v for k, v in resdata}


def parse_dataapi_result():
    result01 = {'record': [[{'longValue': 100}]]}
    result02 = {'record': [[{'isNull': True}]]}

    record = result02['record']
    data = record[0][0].get('longValue')

    logging.info(f'{result01["record"]}')
    logging.info(f'{result02["record"]}')
    logging.info(f'{data}')


if __name__ == '__main__':
    parse_dataapi_result()
