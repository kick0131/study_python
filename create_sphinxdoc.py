import subprocess
"""Sphinxドキュメントコマンド実行スクリプト

    本プログラムを実行するだけで、最新版のSphinxドキュメントを生成します。

    # HTTPサーバ起動して動作確認
    python -m http.server 8000 --directory docs/_build/

"""


def run():
    cmd_api = "sphinx-apidoc -f -o ./docs ./"
    cmd_doc = "sphinx-build -b html ./docs ./docs/_build"

    for cmd in [cmd_api, cmd_doc]:
        result = subprocess.Popen(
            cmd, shell=True, universal_newlines=False)
        print(result)


if __name__ == '__main__':
    run()
