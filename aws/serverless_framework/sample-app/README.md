# sample-app
EventBridgeから定期的にLambdaを叩くサンプル

## usage
```bash
set AWS_PROFILE=xxx
# デプロイ
serverless deploy -v
# 削除
serverless remove -v
```

## notice
`xxx-custom-resource-event-bridge`というLambda関数が追加される。  
- create EventBridge
- mapping Lambda
- attach Lambda permission
をAWS SDKを使って実施している補助関数の用である。CFnを作る作業をServerlessが代行している。
