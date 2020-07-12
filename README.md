python sample
===

* python利用方法
* boto3利用方法

## 準備
* 環境変数PYTHONPATHにaws,basicまでのディレクトリを追加  

* 仮想環境作成  
`python3 -m venv forwin`  
※環境によってはpython3ではなくpython

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
rstファイル生成
`sphinx-apidoc -f -o ./docs .`
rstファイルからhtmlファイル生成
`sphinx-build ./docs ./docs/_build`

