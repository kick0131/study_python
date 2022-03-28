# Cognito sample

## Prepare
### 環境変数
aws/.envに必要な環境変数を配置する事
```bash
AWS_PROFILE=""

# Cognito
COGNITO_USER_POOL_ID=""
COGNITO_CLIENT_ID=""
COGNITO_USER_ID=""
COGNITO_EMAIL=""
COGNITO_PASSWORD=""
COGNITO_CONFIRM_CODE=""
COGNITO_ATTRIBUTES=""
```

### Cognitoアプリクライアント
- シークレットは作成しないこと
- 管理者メソッドを利用する場合、ALLOW_ADMIN_USER_PASSWORD_AUTHはONにすること

