# 各種データ型
# ・リスト
# ・タプル
# ・辞書

import logging
import sys
import json

logging.basicConfig(
    level=logging.DEBUG,            # ログレベル
    format=' %(asctime)s - %(levelname)s - %(message)s')


def listsample():
    """リスト型の動作サンプル

    入れ子の編集、タプルへの変換

    Note:
        基本動作の確認、関数内のコードは都度編集されることを想定。

    """

    logging.debug('=== [{}] start ==='.format(sys._getframe().f_code.co_name))

    # 基本形
    l = [1, 'cat', 3, 'dog']
    for i in range(len(l)):
        print(l[i])

    # 入れ子
    l = [
        [1, 'cat', 3, 'dog'],
        [2, 'lion', 4, 'tiger']
    ]
    print(l)
    for i in range(len(l)):
        for k in range(len(l[i])):
            print(l[i][k])

    # 編集
    l[1][2] = '★★★'
    print(l)

    # 検索
    # loggingモジュールとprintメソッドの出力順に注意
    # print分が出力された後にloggingが出力される
    logging.debug('cat' in l[0])

    # タプルに変換
    l = tuple(l)
    logging.info(type(l))


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
    l = (1, 'cat', 3, 'dog')
    for i in range(len(l)):
        print(l[i])

    # 入れ子
    l = (
        (1, 'cat', 3, 'dog'),
        (2, 'lion', 4, 'tiger')
    )
    print(l)
    for i in range(len(l)):
        for k in range(len(l[i])):
            print(l[i][k])

    # 編集
#    l[1][2] = '★★★'  # NG imutable
#    print(l)

    # 検索
    logging.debug('cat' in l[0])

    # リストに変換
    l = list(l)
    logging.info(type(l))


def dicsample():
    """辞書型の動作サンプル

    入れ子の編集

    Note:
        基本動作の確認、関数内のコードは都度編集されることを想定。

    """

    logging.debug('=== [{}] start ==='.format(sys._getframe().f_code.co_name))

    # 基本形
    # キーが同じものは後勝ちで上書きされる
    l = {'key1': 1, 'key2': 'cat', 'key3': 3, 'key4': 'dog'}
    for i in l.items():
        print(i)

    # 入れ子
    l = {
        'key1': {'key11': 1, 'key12': 'cat', 'key13': 3, 'key14': 'dog'},
        'key2': {'key21': 5, 'key22': 'lion', 'key23': 7, 'key24': 'tiger'}
    }

    # ('key1', {'key11': 1, 'key12': 'cat', 'key13': 3, 'key14': 'dog'})
    #          1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #            2~~~~~~~~  2~~~~~~~~~~~~~  2~~~~~~~~~~  2~~~~~~~~~~~~~
    # 1: 外側のループのvaluesで取得する範囲
    # 2: 内側のループのitemsで取得する範囲
    for i in l.values():
        print(i)
        for k in i.items():
            print(k)

    # 編集
    l['key2']['key22'] = '★★★'
    print(l)

    # 検索
    logging.info('cat' in l['key1'].values())


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
    result={}
    result['data'] = [{"name":"Taro","attr":"Man"},{"name":"Hanako","attr":"Woman"}]

    # 処理ロジック
    newlist =[]
    for dicitem in result['data']:
        locallist=[]
        for value in dicitem.values():
            locallist.append(value)
        newlist.append(locallist)

    # 取得結果確認
    logging.info(newlist)


if __name__ == '__main__':
    logging.error('エラー')
    listdic_extraction()
