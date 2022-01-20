# VIRUSTOTAL
各セキュリティチェッカーサイトを巡回して結果を返してくれる


## API

準備
1. サインアップしてアカウントを取得
1. APIキーを取得([Profile]-[API key])

APIの実行方法
- REST API
- 専用ライブラリを使う

### API KEYについて
本サンプルではpython-dotenvを使用しており、.envファイルに環境変数APIKEYを設定している
```bash
APIKEY=XXXXXX
```

### BASE64エンコード方法
```bash
echo -n https://support.virustotal.com/hc/en-us | openssl enc -e -base64
```

### REST API
[リファレンス](https://developers.virustotal.com/reference)のUNIVERSAL API ENDPOINTSから実行に必要な情報がほとんど得られる。


### ライブラリ
[公式ライブラリ](https://support.virustotal.com/hc/en-us/articles/360006819798-API-Scripts-and-client-libraries)



