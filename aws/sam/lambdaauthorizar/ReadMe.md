## 参考
https://dev.classmethod.jp/articles/lambda-authorizer/

### テンプレート作成
`aws cloudformation package --template-file template.yaml --output-template-file template-output.yaml --s3-bucket XXXXX --profile XXXXX`

- s3バケットは予め用意しておくこと(--s3-bucketオプションの指定先)
- profileオプションはデフォルトプロファイルを使用しない場合のみ利用する

### デプロイ
`aws cloudformation deploy --template-file template-output.yaml --stack-name XXXXX --capabilities CAPABILITY_IAM --profile XXXXX`

- スタック名は任意、CloudFormationのスタック名になる
