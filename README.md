python sample
===

## 作成方針
* サンプルコードは`python 対象ファイル.py`で動作可能とする事
* 利用するVsCode拡張機能など

    | 名称 | 用途 | 備考 |
    |---|---|---|
    | autopep8 | フォーマッタ |---|

## ディレクトリ説明

### aws
Python + AWS

* Cognito
* EC2StartandStop
* SecretManager

### basic
Pythonの基本文法習得用

### docs
Sphinx練習

### usage
その他ライブラリ練習

* psycopg2Sample.py
    PostgreSQL接続


## 準備
* 環境変数PYTHONPATHでmain.pyディレクトリまでのパスを通す

* 仮想環境作成  
`python3 -m venv forwin`  
※ディレクトリ名は環境に応じて適宜読み替える環境によってはpython3ではなくpython

* 仮想環境有効化  
`./forwin/Scripts/activate`  
※vsCodeでactivate実行時にPSSecurityExceptionが発生する場合、PowerShellで以下コマンドを実行  
`Set-ExecutionPolicy RemoteSigned`

* ローカルで必要なデータの配置
aws/_privatejson/cognito_data.json
basic/_ignorefiles


テストデータ格納

## 利用モジュール
boto3

## Sphinx
* rstファイル生成
`sphinx-apidoc -f -o ./docs .`

* rstファイルからhtmlファイル生成
`sphinx-build ./docs ./docs/_build`

