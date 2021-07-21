import argparse

'''
Usage

コマンドライン引数を使用
  python basic/mymain.py -p 123 --addr 192.168.0.1
ヘルプ表示
  python basic/mymain.py -h
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='プログラムの説明')

    parser.add_argument('-p', '--port', help='ポート番号', default='80')
    parser.add_argument('-a', '--addr', help='IPアドレス', default='localhost')
    parser.add_argument('-u', '--user', help='アカウント(user,dev,admin)',
                        choices=['user', 'dev', 'admin'],
                        required=True)

    args = parser.parse_args()

    print(f'addr : {args.addr}')
    print(f'port : {args.port}')
    print(f'user : {args.user}')
