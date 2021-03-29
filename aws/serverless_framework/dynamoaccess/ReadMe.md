## 説明
APIGatewayからFlaskアプリを介してDynamoDBにアクセスする

## 準備

## 実行

デプロイ結果にエンドポイントが出力されるので、出力先に対してcurlを実行
endpoints:
  ANY - https://XXXXX.execute-api.ap-northeast-1.amazonaws.com/dev

- get
curl -H 'Authorization: XXX' <API GW URL>

- post
curl -H 'Authorization: XXX' -d '{"name":"sample","action":"put", "obj":{"key1":"value1", "key2","value2"}}' -H 'Content-Type: application/json' -X POST <API GW URL>

### デプロイ
