python sample
===

## 作成方針
* サンプルコードは`python 対象ファイル.py`で動作可能とする事
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
* EC2StartandStop
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
* 環境変数PYTHONPATHでmain.pyディレクトリまでのパスを通す

    for mac
    ```
    export PYTHONPATH="/Users/hiramatsu/work/study_python:${PYTHONPATH}"
    ```

* 仮想環境作成

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

## 利用モジュール
boto3

## Sphinx
* rstファイル生成
`sphinx-apidoc -f -o ./docs .`

* rstファイルからhtmlファイル生成
`sphinx-build ./docs ./docs/_build`

