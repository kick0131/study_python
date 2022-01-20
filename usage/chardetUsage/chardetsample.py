#!/usr/bin/env python3
import os
import chardet
import glob


def check_fileencode(filepath: str):
    """chardetライブラリを使用したファイルエンコード判定

    複数ファイル指定に対応したファイルエンコード判定処理

    Parameters
    ----------
    filepath : str
        以下いずれかの形式を期待する
        ディレクトリ指定(./tmp)
        拡張子指定(./tmp/*.json)
    """
    files = glob.glob(filepath)
    for file in files:
        chardet_detect(file)


def chardet_detect(filepath: str):
    """chardetライブラリを使用したファイルエンコード判定

    Parameters
    ----------
    filepath : str
        フォーマットチェック対象のファイルパス
    """
    print(f'target : {filepath}')
    with open(filepath, 'rb') as r:
        bynary = r.read()
        print(chardet.detect(bynary))


def main():
    # 自身のファイルパスからの相対パス
    OWN_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(
        OWN_FILE_DIR, *['../../', 'basic', 'data', 'json', 'not_utf8.json'])

    check_fileencode(filepath)


if __name__ == "__main__":
    main()
