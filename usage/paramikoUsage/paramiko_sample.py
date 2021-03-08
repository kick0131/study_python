import sys
import functools
import os
from os.path import join, dirname
# 自作パッケージ
from basic.logutil.loginit import uselogger
# 外部ライブラリ
# pip install paramiko
import paramiko
# pip install python-dotenv
from dotenv import load_dotenv

logger = uselogger(__name__)

# 環境変数を外部ファイルから取得
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

HOST = os.environ.get("SSH_HOST")
USER = os.environ.get("SSH_HOST_USER")
PASS = os.environ.get("SSH_HOST_PASSWORD")
EC2HOST = os.environ.get("EC2_HOST")
EC2USER = os.environ.get("EC2_HOST_USER")


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


class dummyclass:
    def __init__(self):
        pass

    def __repr__(self):
        return f'{__class__}.{__name__}'

    def __enter__(self):
        pass

    def __exit__(self):
        pass


def ec2login():
    # SSH秘密鍵のパス
    keyfilepath = join(dirname(__file__), 'AmazonLinuxEC2.pem')
    logger.info(f'keyfilepath:{keyfilepath}')

    # EC2にSSHログインしてコマンドを実行する
    with paramiko.SSHClient() as client:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(EC2HOST, username=EC2USER, key_filename=keyfilepath)
        stdin, stdout, stderr = client.exec_command('uname -a')
        for line in stdout:
            print(line)


@trace
def main():
    logger.info('Hello')

    with paramiko.SSHClient() as client:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(HOST, username=USER, password=PASS)
        stdin, stdout, stderr = client.exec_command('uname -a')
        stdin, stdout, stderr = client.exec_command('cat /etc/resolv.conf')
        for line in stdout:
            print(line)


if __name__ == '__main__':
    print(sys._getframe().f_code.co_name + '__main__')
    ec2login()
