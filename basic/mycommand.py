import subprocess
from logging import StreamHandler, Formatter, INFO, getLogger
import os
import json

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


def tshark_cmd():
    """パケットキャプチャファイル(pcap)を扱うtsharkを使うパターン

    tsharkコマンドは別途インストールが必要

    コマンドライン上は以下だが、サブプロセスはリダイレクトを扱えないので
    output引数を利用する
    tshark -nr {PCAP_FILE} -T json > {JSON_FILE}

    """
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PCAP_FILE = os.path.join(BASE_DIR, 'hoge.pcap')
    EXE_CMD = f'tshark -nr {PCAP_FILE} -T json'

    # ファイル出力させる場合
    # with open('out.txt', 'w') as fp:
    #     result = subprocess.run(EXE_CMD.split(' '),
    #                             timeout=3,
    #                             encoding='utf-8',
    #                             stdout=fp)

    # 処理内でJSONを扱う場合
    json_str = subprocess.check_output(EXE_CMD.split(' ')).decode('utf-8')
    tshark_pkts = json.loads(json_str)

    # 要素アクセス例、list<dict>型である点に注意
    getLogger().info(f'tshark_pkts: {type(tshark_pkts)}')
    getLogger().info(f'tshark_pkts[0]: {type(tshark_pkts[0])}')
    getLogger().info(
        f'tshark_pkts[0]._source.layers.eth.eth.dst: {tshark_pkts[0]["_source"]["layers"]["eth"]["eth.dst"]}')


if __name__ == "__main__":
    call_for_win()
