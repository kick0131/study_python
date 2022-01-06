#!/usr/bin/env python3
import os
import chardet


def main():
    # 自身のファイルパスからの相対パス
    OWN_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(
        OWN_FILE_DIR, *['../../', 'basic', 'data', 'json', 'not_utf8.json'])

    # normal_str = 'hello'
    # binary_str = b'\x83X\x83}\x83J\x83\x81'
    # chardet.detect(normal_str)
    # chardet.detect(binary_str)
    with open(filepath, 'rb') as r:
        bynary = r.read()
        print(chardet.detect(bynary))


if __name__ == "__main__":
    main()
