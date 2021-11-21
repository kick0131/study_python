# python sample
===

## ToDo
- pyyaml
- absl-py
- pytz
- psutil
- aiohttp
- asyncio

## 作成方針
* サンプルコードは`python 対象ファイル.py`で動作可能とする事
* basicを除いてディレクトリ内で処理が完結する事
* 利用するVsCode拡張機能など

    | 名称 | 用途 | 備考 |
    |---|---|---|
    | autopep8 | フォーマッタ |---|
    | flake8 | コードチェック |---|
    | Sphinx | ドキュメント生成 |---|

* 使用ライブラリ

    | 名称 | 用途 | 備考 |
    |---|---|---|
    | flake8 | コードチェック |---|
    | sphinx | ドキュメント生成 |---|
    | jupyterlab | jupyterサーバ |---|
    | boto3 | AWS CLIのPythonラッパー |---|


* ローカルで必要なデータの配置
    - aws/_privatejson/cognito_data.json
    - basic/_ignorefiles


### flake8設定
python.linting.pylintEnabled　無効  
python.linting.flake8Enabled　有効

## ディレクトリ説明
```
    /aws    AWS SDK(boto3)
    /basic  標準モジュール
    /docs   Sphinx
    /usage  3rdPartyモジュール
    /pytest pytest練習
    /requirements requirements.txt参照先
```


# 準備
## 環境変数
* 環境変数PATHにpythonのパスを通す
    `python -m site --user-site`の出力(XXXX/Scripts)

### linux mac
* 環境変数PYTHONPATHでmain.pyディレクトリまでのパスを通す
    ```
    export PYTHONPATH="/Users/hiramatsu/work/study_python:${PYTHONPATH}"
    ```

# 仮想環境
## venv
Pipenvも過去に使っていたが、公式も非推奨とした為、  
標準でついてくるvenvを利用する方針に切り替え

### 環境構築
```
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

※ディレクトリ名は環境に応じて適宜読み替える。  
環境によってはpython3ではなくpython

- 仮想環境有効化  
    `./.venv/bin/activate`  
    ※vsCodeでactivate実行時にPSSecurityExceptionが発生する場合、PowerShellで以下コマンドを実行  
    `Set-ExecutionPolicy RemoteSigned`



