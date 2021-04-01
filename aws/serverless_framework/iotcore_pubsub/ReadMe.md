## 説明
本ディレクトリはIoTCoreを使ったPublish、Subscribe動作確認プロジェクトです

## 準備
### requirementsプラグインのインストール
serverless-python-requirements

### requirementsファイル
awsiotsdk

### 送信先IoTCoreの用意
- モノの作成
- 証明書の作成、DL
- ポリシーの作成
- モノに証明書をアタッチ
- 証明書にポリシーをアタッチ
- エンドポイントをメモ

### [Mac環境のみ]Docker上のLinuxでライブラリをインストール
docker run --rm -v $(pwd):/work -w /work python:3.8 pip install -r requirements.txt -t .
このファイルをLambdaLayer化する
(layer/python配下に配置)

### 仮想環境(ローカルで動かす場合のみ)
- 環境作成（初回のみ）
pipenv --python 3
- 仮想環境にログイン
pipenv shell
- AWSIoTSDKforPythonライブラリのインストール
pipenv install awsiotsdk

## 実行
### AWSCLIからPublishメッセージ送信し、作成したIoTRuleを動かす
aws iot-data publish --topic iot-serverless-topic --payload file://sample.json --profile XXXXX

### endpoint
`aws iot describe-endpoint --endpoint-type iot:Data-ATS --profile XXX`
