# AWS IoT SDK for Python v2
https://github.com/aws/aws-iot-device-sdk-python-v2

## 準備
### AWS IoT SDK v2をサブモジュールとして取り込み
`git submodule add https://github.com/aws/aws-iot-device-sdk-python-v2`

### middle ware
- awsiotsdk v2
`pip install awsiotsdk`

## 実行順序
- 最新のdockerイメージを用意

    `docker build -t amazonlinux-iot .`

- docker run

    `docker run -it --rm --mount type=bind,src=$(pwd),dst=/data kick0131/amazonlinux-iot /bin/bash`

- 各クライアントプログラム実行

### PubSubサンプル
AWSコンソールのIoTCore-テストからサブスクライブで確認可能
`python3 aws-iot-device-sdk-python-v2/samples/pubsub.py --endpoint <endpoint> --root-ca <rootca file> --cert <.cert file> --key <.pem file>`

### フリートプロビジョニング実行
`python3 aws-iot-device-sdk-python-v2/samples/fleetprovisioning.py --endpoint <endpoint> --root-ca root-CA.crt --cert <.cert file> --key <.pem file> --templateName <tempname> --templateParameters "{\"SerialNumber\": \"001\" , \"AWS::IoT::Certificate::Id\": \"<cert hash>\"}"`

- 証明書が２つ作成される
- MyPrefix_(引数のシリアルNo)でモノが作成される
- fleattemplate-XXXXXXXXでポリシーが作成される(テンプレートでポリシーのアタッチを行った場合)
- これらの処理は上書きで実行される
