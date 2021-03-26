## 説明
APIGatewayからFlaskアプリを介してDynamoDBにアクセスする

## 準備

## 実行

デプロイ結果にエンドポイントが出力されるので、出力先に対してcurlを実行
endpoints:
  ANY - https://XXXXX.execute-api.ap-northeast-1.amazonaws.com/dev

- post
curl -d '{"name":"sample","action":"put"}' -H 'Content-Type: application/json' -X POST <API GW URL>

### デプロイ
