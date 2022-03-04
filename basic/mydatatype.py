import logging
import sys
import re
import os
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


def listdic_create():
    """リスト内辞書データの連結作成

    リスト内に辞書型が組合された場合の動作サンプル。
    主にjsonを想定したケース。

    Returns:
        連結された辞書データ

    .. note:
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

    .. note:
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
    """文字列から特定キーワードを除去する
    """
    KEYWORD = 'Bearer'
    before_str = []
    before_str.append(' Bearer XXXX.YYYY.ZZZZ')  # OK
    before_str.append('Bearer XXXX.YYYY.ZZZZ')  # OK
    before_str.append(' XXXX.YYYY.ZZZZ')        # NG
    before_str.append('XXXX.YYYY.ZZZZ')         # NG

    # 同じディレクトリに存在するファイルを指定
    tokenfilepath = os.path.join(os.path.dirname(__file__), 'bearer')
    with open(tokenfilepath, mode='r', encoding='utf_8') as f:
        before_str.append(f.read())

    # 特定キーワードを除外
    regex_str = f".*({KEYWORD}) "
    for line in before_str:
        if KEYWORD in line:
            logging.info(f'before : {re.sub(regex_str, "", line)}')


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


def get_dict_hierarchy():
    """辞書型の階層構造データを取得する効率的な方法
    """
    hierarchy = {
        'key1': {
            'key2': {
                'key3': 'hello world'
            }
        }
    }

    val = hierarchy.get('key1', {}).get('key2', {}).get('key3', '')
    if val is None:
        val = ''

    logging.info(f'{val}')


def dict_comprehension():
    """辞書型の内包表記
    """
    # set型
    humans = {name for name in ['taro', 'jiro', 'saburo']}
    # 辞書型(同じキーに上書きされるので、結局要素は1つ)
    humans2 = {'hoge': name for name in ['taro', 'jiro', 'saburo']}
    print(humans)
    print(f'type: {type(humans)}')
    print(humans2)
    print(f'type: {type(humans2)}')


def dict_filtering():
    """辞書型のフィルタリング

    {
        "name":"taro",
        "age":10,
        "moreinfo":{
            "country":"japan",
            "addr": {
                "capital" : "tokyo",
                "word" : "chiyodaku"
            }
        }
    }

    から

    {
        "addr": {
            "capital" : "tokyo",
            "word" : "chiyodaku"
        }
    }
    を作る
    """
    human_info = {
        "name": "taro",
        "age": 10,
        "moreinfo": {
            "country": "japan",
            "addr": {
                "capital": "tokyo",
                "word": "chiyodaku"
            }
        }
    }

    # 取得元キーのパス
    # 新規作成時に割り当てるキーのパス
    # 存在しないパスはスキップする動作を期待
    mapping_list = [
        ['moreinfo.addr.capital', 'addr.capital'],
        ['moreinfo.addr.word', 'word'],
        ['xxx.yyy.zzz', 'word'],
    ]

    new_dict = {}
    for before, after in mapping_list:
        # print(f'befor :{before}')
        # print(f'after :{after}')
        # beforeのキーパスからvalueを取得
        value = get_dictval(human_info, before.split('.'))
        if value is not None:
            # afterのキーパスにvalueを設定
            set_dictval(new_dict, after.split('.'), value)

    print(new_dict)


def get_dictval(target_dict: dict, keys: list):
    """辞書型からの値取得処理（ネスト対応）

    Parameters
    ----------
    target_dict : dict
        取得元辞書
    keys : list
        アクセス元キー名。ネストされた場合は複数要素となる
        ex)
        A : {
            B : value
        }
        の場合、['A','B']の入力を期待する

    Returns
    -------
    any
        取得した値
    """
    # print(f'get_dictval keys:{keys}')
    if len(keys) >= 2:
        key = keys.pop(0)
        if key in target_dict:
            return get_dictval(target_dict[key], keys)
        else:
            return None
    else:
        return target_dict.get(keys.pop(0))


def set_dictval(target_dict: dict, keys: list, value):
    """辞書型へ値の設定処理（ネスト対応）

    階層構造化した辞書型のキーパスに値を設定する

    Parameters
    ----------
    target_dict : dict
        設定先辞書
    keys : list
        階層化されたキー名で分割されたリスト
    value : any
        設定値

    Returns
    -------
    func or None
        キーパスが残っている間、本メソッドで再帰する
    """
    # print(f'set_dictval keys:{keys} value : {value}')
    if len(keys) >= 2:
        key = keys.pop(0)
        if key not in target_dict:
            target_dict[key] = {}
        return set_dictval(target_dict[key], keys, value)
    else:
        target_dict[keys.pop(0)] = value
        return None


if __name__ == '__main__':
    # dict_filtering()
    pass
