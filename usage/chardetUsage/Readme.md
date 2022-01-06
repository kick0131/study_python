# 文字コード判別ライブラリ
https://github.com/chardet/chardet

```
pip install chardet
```

## Usage
バイナリで読み込んだファイルポインタを使ってchardet.detectメソッドを実行

```python
with open(filepath, 'rb') as r:
    bynary = r.read()
    print(chardet.detect(bynary))
```

## What's decode?
https://docs.python.org/ja/3/library/stdtypes.html?#bytes.decode

```python
bytes.decode(encoding='utf-8', errors='strict')
```
引数なしの場合、エンコードはutf-8で厳密なチェックを行う  

https://docs.python.org/ja/3/library/codecs.html#error-handlers

|errors|内容|
|--|--|
|strict|UnicodeError例外を出す|
|ignore|エンコードできない文字を読み飛ばす|
|replace|REPLACEMENT CHARACTERと呼ばれるU+FFFD(※)に変換される|

※ \xef \xbf \xbdと同義

## Links
- [行単位でバイナリを読む](https://blog.amedama.jp/entry/2015/11/25/232855)
- [【公式】 PythonのUNICODE](https://docs.python.org/3/howto/unicode.html)

## License
LGPL2.1
