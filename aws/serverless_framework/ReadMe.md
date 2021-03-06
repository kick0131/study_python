## 説明
本ディレクトリはServerlessFrramework作業用ディレクトリです

## 準備
### 前提条件
- **node.js**がインストールされていること
- 対象クラウドサービスの実行アカウントが生成されていること

AWSの場合は`aws configure --profile XXXXX`などでアクセスキーを登録しておくと便利

### インストール
serverlessコマンド未インストールの場合
```
npm install -g serverless
```
serverlessコマンドの短縮系が`sls`

package-lock.jsonがある場合は追加で実行
```
npm install
```

### 環境作成
```
sls create --template aws-python3 --name myservice --path myservice01 
```
- template で対象のクラウドサービスとその上で実行するアプリの種類を指定
- path で作業ディレクトリを指定
- name でサービス名を定義

## 実行
### デプロイ
sls.ymlがあるディレクトリで以下コマンドを実行
```
sls deploy -v --aws-profile XXXXX
```
### 削除
AWSリソースが全て消えるので注意
```
sls remove -v --aws-profile XXXXX 
```


## プラグイン

### serverless-wsgi
WebServerGatewayInterface(ウィスキー)対応のアプリケーションに変換するプラグイン

```
sls plugin install -n serverless-wsgi
```
