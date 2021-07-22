# python sample
===

## ToDo

- pyyaml
- absl-py
- pytz
- psutil


## 作成方針
* サンプルコードは`python 対象ファイル.py`で動作可能とする事
* basicを除いてディレクトリ内で処理が完結する事
* 利用するVsCode拡張機能など

    | 名称 | 用途 | 備考 |
    |---|---|---|
    | autopep8 | フォーマッタ |---|
    | flake8 | コードチェック |---|
    | Sphinx | ドキュメント生成 |---|

### flake8設定
python.linting.pylintEnabled　無効
python.linting.flake8Enabled　有効

### コメントルール

## ディレクトリ説明

### aws
Python + AWS

* Cognito
* EC2
* SecretManager

### basic
Pythonの基本文法習得用

### docs
Sphinx練習

- 使い方
```
sphinx-apidoc -f -o ./docs .
sphinx-build -b html ./docs ./docs/_build  
```

### usage
その他ライブラリ練習

* psycopg2Sample.py
    PostgreSQL接続


## 準備
* [win]環境変数PATHにpipenvのパスを通す
    `python -m site --user-site`の出力(XXXX/Scripts)


* 環境変数PYTHONPATHでmain.pyディレクトリまでのパスを通す

    for mac
    ```
    export PYTHONPATH="/Users/hiramatsu/work/study_python:${PYTHONPATH}"
    ```

* 仮想環境作成

    - 使用するライブラリ
    | 名称 | 用途 | 備考 |
    |---|---|---|
    | flake8 | コードチェック |---|
    | sphinx | ドキュメント生成 |---|
    | jupyterlab | jupyterサーバ |---|

    - pipenv
        ```
        pip install pipenv
        pipenv --version 3
        ```

        - pipenv導入後はPipfileがあるディレクトリで以下を実行することで環境の再現が可能

        ```
        pipenv shell
        pipenv install
        ```

    - venv

        `python3 -m venv forwin`  
        ※ディレクトリ名は環境に応じて適宜読み替える。環境によってはpython3ではなくpython

        - 仮想環境有効化  
        `./forwin/Scripts/activate`  
        ※vsCodeでactivate実行時にPSSecurityExceptionが発生する場合、PowerShellで以下コマンドを実行  
        `Set-ExecutionPolicy RemoteSigned`

* ローカルで必要なデータの配置
    - aws/_privatejson/cognito_data.json

    - basic/_ignorefiles


テストデータ格納

## Pipenvコマンド 
    | 名称 | 用途 | 備考 |
    |---|---|---|
    | install | パッケージのインストール |---|
    | run | Pythonのコマンド実行 |---|
    | shell | 仮想環境起動 |---|
    | update | piplockファイルの同期 |---|
    | update | Pipenv.lockに記載されていない全てのパッケージをアンインストール |---|


## 利用モジュール
boto3

## Sphinx
* rstファイル生成
`sphinx-apidoc -f -o ./docs .`

* rstファイルからhtmlファイル生成
`sphinx-build ./docs ./docs/_build`

# Jupyter

## カーネルをpipenvの環境に変更
(引用)https://qiita.com/mzn/items/99d769d0ad9d03a5d73e
```
pipenv shell
python -m ipykernel install --user --name=<お好きな名前>
```
jupyter接続後、インタープリタをpipenv環境のpythonに指定

## 実行方法
1. (vscodeとは別のターミナルで実行)pipenv環境（Jupyterインストール済）で以下コマンドを実行
    ```
    jupyter lab
    ```
    Jupyterが起動し、自動でブラウザからJupyterにアクセスする

2. notebookを開き、右上のJupyterServerから手順１で立ち上げたJupyterServerを選択する


# その他
### pipenvのパッケージ削除
`Pipfile`から不要なパッケージを削除し、`pipenv clean`を実行する

