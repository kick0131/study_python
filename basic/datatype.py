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

# --------------------------------------------------------
# リスト型
# --------------------------------------------------------


def listsample():
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
    """ 空要素を判定する
    """
    mylist = []
    if not mylist:
        logging.info('None!!')
    else:
        logging.info('Exists!!')


# --------------------------------------------------------
# タプル型
# --------------------------------------------------------


def tuplesample():
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

# --------------------------------------------------------
# 辞書型
# --------------------------------------------------------


def dicsample():
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

    Args:
        無し

    Returns:
        連結された辞書データ

    Raises:
        無し

    Examples:
        無し

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


# --------------------------------------------------------
# main
# --------------------------------------------------------
# listsample()
# tuplesample()
# dicsample()
# param = listdiccreate()
# logging.info(json.dumps(param))
listisEmpty()
