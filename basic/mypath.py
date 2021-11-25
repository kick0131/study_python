import os

'''
パスいろいろ

'''

if __name__ == '__main__':
    samplepath = __file__
    samplepath_rel = os.path.relpath(__file__)
    print(f'自身のパス(__file__)     : {samplepath}')
    print(f'ディレクトリ名           : {os.path.dirname(samplepath)}')
    print(f'ファイル名               : {os.path.basename(samplepath)}')
    print(f'相対パス                 : {os.path.relpath(samplepath)}')
    print(f'相対パスから絶対パスに変換 : {os.path.abspath(samplepath_rel)}')
    print(f'パスの結合               : {os.path.join(os.getcwd(), "hello")}')
    print(f'パスの結合               : {os.path.join(os.getcwd(), "hello/")}')
