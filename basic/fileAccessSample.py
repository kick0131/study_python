import os
import pprint
import traceback


def createDir(dirpath: str):
    """
    ディレクトリが無ければ作成
    絶対パス、相対パス両対応
    mkdir -p 相当
    中間ディレクトリが無い場合はそこから作成する。
    ファイルが指定された場合、中間ディレクトリを生成する
    """

    # ディレクトリ部を取得
    createPath = os.path.dirname(dirpath)

    # ディレクトリが無ければ作成
    if not os.path.exists(createPath):
        pprint.pprint('=== not createPath')
        # 相対パスを絶対パスに変換
        if not os.path.isabs(createPath):
            pprint.pprint('=== not ABS')
            createPath = os.path.abspath(createPath)
        pprint.pprint('createPath:{}'.format(createPath))
        os.makedirs(createPath)

    return


def mvSample():
    """ディレクトリ、ファイルの移動
    """
    return


def rmSample():
    """ディレクトリ、ファイルの削除
    """
    return


def copySample():
    """ディレクトリ、ファイルのコピー
    """
    return


def sampleRun():
    """サンプル関数
    """
    result = 'success'
    print('os.getcwd:{} sep:{}'.format(os.getcwd(), os.sep))

    try:
        createDir(r'log/logA/sample.log')

    # とにかく補足
    except Exception:
        # スタックトレースは出すべき
        pprint.pprint('== Error occured reason:{}'.format(
            traceback.format_exc()))
        result = 'Error'

    else:   # 正常終了 本来やりたい事
        pass

    finally:  # 強制実行 どうしてもやる必要のある事
        pass  # 何もしない場合の構文

    return result


# メイン処理
if __name__ == '__main__':
    print("result:{0}".format(sampleRun()))
