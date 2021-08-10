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

### basic
Pythonの基本文法習得用

### docs
Sphinx

### usage
その他ライブラリ練習

---
# 準備
## 環境変数
### win
* 環境変数PATHにpipenvのパスを通す
    `python -m site --user-site`の出力(XXXX/Scripts)

### linux mac
* 環境変数PYTHONPATHでmain.pyディレクトリまでのパスを通す
    ```
    export PYTHONPATH="/Users/hiramatsu/work/study_python:${PYTHONPATH}"
    ```

## 仮想環境

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
    ※ディレクトリ名は環境に応じて適宜読み替える。  
    環境によってはpython3ではなくpython

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

# その他
### pipenvのパッケージ削除
`Pipfile`から不要なパッケージを削除し、`pipenv clean`を実行する

