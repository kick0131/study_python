import os
import zipfile
from logging import StreamHandler, Formatter, INFO, getLogger

"""ZIP処理
    data/zipsample.zipを使ったzip操作

    ZIPの中身は無害なファイル
    ---
    zipsample
        empty
        folderA
            hello1.txt
            hello2.txt
            hello3.txt
    ---
"""


DATA_DIR = os.path.dirname(os.path.abspath(__file__)) + './data'
ZIP_PATH = os.path.join(DATA_DIR, 'zipsample.zip')
EXTRACT_PATH = os.path.join(DATA_DIR, 'extract/')


def init_logger():
    """ロガー初期化

    初期化後、getLogger().info('hello')の様に使う

    """
    handler = StreamHandler()
    handler.setLevel(INFO)
    handler.setFormatter(
        Formatter("[%(asctime)s] [%(threadName)s] %(message)s"))
    logger = getLogger()
    logger.addHandler(handler)
    logger.setLevel(INFO)


def check_zip(filepath: str):
    if zipfile.is_zipfile(filepath) is False:
        getLogger().error(f'zipファイルではない : {filepath}')
        return

    with zipfile.ZipFile(filepath) as existing_zip:
        # パス一覧
        # for name in existing_zip.namelist():
        #     getLogger().info(f'name : {name}')

        # 特定ディレクトリ配下のZIPパスを抽出
        zippath = 'zipsample/folderA/'
        zippathlists = [name for name in existing_zip.namelist()
                        if zippath in name]
        for zippath in zippathlists:
            getLogger().info(f'name : {zippath}')
            if existing_zip.getinfo(zippath).is_dir() is True:
                getLogger().info('ディレクトリパス')
                continue
            # ファイル解凍
            # zippathがそのまま展開先ディレクトリに渡される
            # 例
            # /data/zipsample/folderA/hello.txt
            existing_zip.extract(zippath, path=EXTRACT_PATH)

        # 解凍後のファイルパス総数(フォルダ含む)
        # getLogger().info(f'filelen : {len(existing_zip.namelist())}')


def main():
    init_logger()

    check_zip(ZIP_PATH)


if __name__ == "__main__":
    main()
