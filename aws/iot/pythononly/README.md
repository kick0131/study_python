# iot core sample
[公式](https://aws.amazon.com/jp/premiumsupport/knowledge-center/iot-core-publish-mqtt-messages-python/)

## setup
```bash
pip install awsiotsdk
```
1. certディレクトリを用意し、その中に
  - 秘密鍵
  - デバイス証明書
  - ルート証明書
  を格納

## start
CLIENT_IDは任意、TOPICはIoT Coreで許可されている値
```bash
# publish実行
python pubsub.py

# エンドポイント確認
aws iot describe-endpoint --endpoint-type iot:Data-ATS --profile <myprofile>
```
