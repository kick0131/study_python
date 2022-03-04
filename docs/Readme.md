# Sphinx操作

## ディレクトリ構成
```
(root)
+ hoge
| + huga.py
|
+ doc
  + _build
  + xxx.rst
  + conf.py
  + 以下略
```

### 流れ
rootディレクトリで実行すること
1. conf.pyに従ったrstファイルを出力
    ```bash
     sphinx-apidoc.exe -f -o .\docs .
    ```
1. rstファイルからHTMLファイルを出力する
    ```bash
    sphinx-build.exe -b html .\docs .\docs\_build
    ```
1. (必要に応じて)HTTPサーバで生成したHTMLを確認
    ```bash
    python -m http.server 8000 --directory docs/_build/
    ```

## 主要ファイル

### conf.py
- Sphinx対象ファイルの定義
- Sphinxに対するオプション定義


### index.rst
Sphinx出力時のトップディレクトリに相当
ここに必要なモジュールを追加していく
```
.. toctree::
   :maxdepth: 4
   :caption: Contents:

   main
   sample/sample1
   aws
   aws.Cognito
   aws.EC2StartandStop
   aws.SecretManager
   basic
   modules
```



## その他
### テーマの変更
1. ライブラリインストール  
`pip install sphinx-rtd-theme`

1. `conf.py`の変更
```python
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.napoleon',
]
html_theme = 'sphinx_rtd_theme'
```
