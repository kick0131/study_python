import subprocess
from logging import StreamHandler, Formatter, INFO, getLogger

"""CLI実行方法
"""


def init_logger():
    handler = StreamHandler()
    handler.setLevel(INFO)
    handler.setFormatter(
        Formatter("[%(asctime)s] [%(threadName)s] [%(levelname)s] %(message)s"))
    logger = getLogger()
    logger.addHandler(handler)
    logger.setLevel(INFO)


def call_for_win():
    """windows上でコマンドプロンプトを実行するサンプル
    """
    init_logger()
    getLogger().info('start')
    try:
        # Popenとrunどちらの方法でも実行可能、run推奨
        subprocess.Popen('dir', shell=True)

        # タイムアウト待ちを行い、エラーを発生させる例
        # subprocess.run(['timeout', '/T', '2'], shell=True, timeout=1)

    except Exception as e:
        getLogger().error(e)

    getLogger().info('end')


def call_for_linux():
    """linux上でコマンドプロンプトを実行するサンプル
    """
    init_logger()
    getLogger().info('start')
    try:
        # Popenとrunどちらの方法でも実行可能、run推奨
        subprocess.Popen('ls')

        # タイムアウト待ちを行い、エラーを発生させる例
        # subprocess.run(['sleep', '2'], timeout=1)

    except Exception as e:
        getLogger().error(e)

    getLogger().info('end')


if __name__ == "__main__":
    call_for_win()
