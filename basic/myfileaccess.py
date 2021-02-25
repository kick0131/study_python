import os
import pprint
import traceback
import shutil


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


def rmSample(delPath: str):
    """ディレクトリ、ファイルの削除

    rm -rf相当の動作を期待する

    Parameters
    ----------
    delPath : str
        削除対象のディレクトリまたはファイルパス
    """
    # ディレクトリ部,ファイル名を取得
    dirname, basename = os.path.split(delPath)

    # ファイル名が入力されている場合、ファイル指定されたと判断し、ファイルを削除する
    if len(basename) != 0:
        if os.path.exists(delPath):
            os.remove(delPath)
        else:
            print(f'ERROR filepath is not exists.({delPath})')
    # ディレクトリ名のみ入力されている場合、ディレクトリ指定されたと判断し、再帰削除を行う
    elif len(dirname) != 0:
        if os.path.exists(dirname):
            shutil.rmtree(dirname)
        else:
            print(f'ERROR dirpath is not exists.({dirname})')
    # 上記以外の場合はエラー
    else:
        print(f'ERROR arg is wrong.{os.getcwd()} {os.sep}')
        return

    print(f'Successfly remove {delPath}')
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
    # print("result:{0}".format(sampleRun()))

    # remove file path
    rmfilepath = os.getcwd() + '/log/logA/'
    rmSample(rmfilepath)
