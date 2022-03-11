import platform
import os
import boto3

'''試験対象

pymockから内容を書き換える事を確認する為のサンプルクラス、モジュール

'''

CONST_VALUE = 'this is const'
MYTIMEOUT_MESSAGE = '100ms over'
region = os.getenv('AWS_REGION')


class BaseException(Exception):
    """ユーザ定義例外基底クラス
    """
    pass


class MyTimeoutError(BaseException):
    """自作例外1
    """
    pass


def get_platform():
    return platform.system()


def exception_sample():
    raise MyTimeoutError(MYTIMEOUT_MESSAGE)


def get_env():
    return region


def plus(a: int, b: int):
    return a + b


def funcname(func):
    """デコレータを使った関数ログ
    """
    funcname = func.__name__

    def _wrapper(*args, **kwargs):
        print(f'=== {funcname} start')
        result = func(*args, **kwargs)
        print(f'=== {funcname} end')
        return result
    return _wrapper


class BaseClass:
    @funcname
    def basefunc01(self):
        print('test method called')
        return 'ABC'


def targetdynamo(writelist: list, tblname: str):
    """pytestお題_インスタンスのネスト構造

    put_itemの引数をAssertで検証したい場合、どのように書けばよいか？

    ポイント
    boto3.resourceのモック化はmocker.patch('boto3.resource')で問題ない。
    その後のインスタンスがTableを読んだ際の戻り値、
    更にその戻り値がbatch_writerを読んだ戻り値でメソッドを実行させている為、
    多段呼び出し階層のcall_argsが単純に取れない。

    Args:
        writelist (list): 書き込みデータ。json(dict)の配列を想定
        tblname (str): テーブル名
    """

    # DynamoDBクライアント設定
    dynamodb = boto3.resource("dynamodb", region_name=region)

    # DynamoDB登録処理(IoTデータストア)
    table_iotdata = dynamodb.Table(tblname)
    with table_iotdata.batch_writer() as batch:
        for data in writelist:
            batch.put_item(Item=data)


if __name__ == '__main__':
    target = BaseClass()
    print(f'test method result : {target.basefunc01()}')
    print(f'{get_platform()}')
