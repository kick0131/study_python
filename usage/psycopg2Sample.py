import sys
from pprint import pprint
import json
import functools
# 外部ライブラリ
# pip install psycopg2
import psycopg2


def trace(func):
    """[sample]可変長引数を取るデコレータ
    """

    # メタデータもデコレートする（ベストプラクティスの一部）
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        return original_result
    return wrapper


def local(func):
    """ローカル環境切り替え用デコレータ

    第1引数(lambda_handlerの引数event）の内容を書き換える

    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 接続情報をEC2からのSSH転送情報に書き換え
        json_dict = json.loads(args[0])
        json_dict['port'] = 55432
        json_dict['host'] = 'localhost'
        newargs = (json_dict, args[1])
        original_result = func(*newargs, **kwargs)
        return original_result
    return wrapper


def main():
    # メイン呼び出し

    # leventの内容
    # event['port']
    # event['host']
    # event['database']
    # event['username']
    # event['password']
    # levent = [{'port':80,'host':'host','database':'dev','username':'test','password':'test'}]
    levent = None
    lcontext = "context"
    lambda_handler(levent, lcontext)


@local
def lambda_handler(event, context):
    print(sys._getframe().f_code.co_name + '__main__')

    try:
        print('before connect')
        connection = psycopg2.connect(
            port=event['port'], host=event['host'], database=event['database'], user=event['username'], password=event['password'])

        print('createcur')
        with connection.cursor() as createcur:
            createcur.execute(
                "insert into t_typesample values( 1,'サンプルビル', 101, 123.0123456789, 140.321, 40.321, current_timestamp)")

        print('cur')
        with connection.cursor() as cur:
            cur.execute("select * from t_typesample")
            result = ''
            for row in cur:
                result += ", ".join(map(str, row)) + "\n"

            pprint(result)

        print('delcur')
        with connection.cursor() as delcur:
            delcur.execute(
                "delete from t_typesample where building_name = 'サンプルビル'")

        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }

    except Exception as e:
        print(e)
        raise e


if __name__ == '__main__':
    print(sys._getframe().f_code.co_name + '__main__')
    main()
