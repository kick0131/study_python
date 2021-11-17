import os
import pprint
import traceback
import shutil


def overrapped(func):
    """デコレータ動作サンプル

    Parameters
    ----------
    func : func
        デコレートされる関数に置き換わる仮引数

    Returns
    -------
    none
        別の関数を呼び出すだけで値を戻さない
    """
    def wrapper(*args, **kwargs):
        dirpath = os.getcwd() + '/log/logA/'
        filename = 'hogehoge'
        increamentFile(dirpath, filename, args[0])
    return wrapper


@overrapped
def dummy_func(data, category, unit, interval, end_date):
    pass


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


def increamentFile(dirpath: str, filename: str, data: str):
    """
    指定ディレクトリにファイルを生成する。
    <dirpath>/<filename>_XXXX(Xは数字)とし、
    同名のファイルが存在する場合はサフィックスをインクリメントしたファイル名とする。

    準正常
    サフィックスが最大値で重複した場合
    ディレクトリが存在しない場合
    ファイル名が空文字の場合
    """
    if not os.path.exists(dirpath):
        raise ValueError("dirpath is not exists.")
    if len(filename) == 0:
        raise ValueError("filename is Empty.")

    # ファイルのフルパス生成
    basefilepath = os.path.join(dirpath, filename)

    # 0000からサフィックスをインクリメントして重複しないファイルがあれば作成
    for i in range(10):
        suffix = f'_{i:04}'
        createfile = basefilepath + suffix
        if os.path.exists(createfile):
            pprint.pprint(f'=== {createfile} is exists')
            continue

        # ファイル生成
        with open(createfile, 'w') as f:
            if len(data) == 0:
                print("create empty file.")
            f.write(data)
        return
    raise Exception('All file exists.')


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
            raise Exception(f'ERROR filepath is not exists.({delPath})')
    # ディレクトリ名のみ入力されている場合、ディレクトリ指定されたと判断し、再帰削除を行う
    elif len(dirname) != 0:
        if os.path.exists(dirname):
            shutil.rmtree(dirname)
        else:
            raise Exception(f'ERROR dirpath is not exists.({dirname})')
    # 上記以外の場合はエラー
    else:
        raise Exception(f'ERROR arg is wrong.{os.getcwd()} {os.sep}')

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
    except Exception as e:
        # スタックトレースは出すべき
        pprint.pprint('== Error occured reason:{}'.format(
            traceback.format_exc()))
        raise e

    else:   # 正常終了 本来やりたい事
        pass

    finally:  # 強制実行 どうしてもやる必要のある事
        pass  # 何もしない場合の構文

    return result


# メイン処理
if __name__ == '__main__':
    # print("result:{0}".format(sampleRun()))
    filepath = os.getcwd() + '/log/logA/'

    # dummy
    dummy_func('hoge', None, None, None, None)
    dummy_func('ABCDE', None, None, None, None)
    dummy_func('dummy', None, None, None, None)

    # create directry
    # createDir(filepath)

    # create file
    filename = 'hogehoge'
    for i in range(3):
        increamentFile(filepath, filename, 'huga')

    # remove file path
    # rmSample(filepath)
