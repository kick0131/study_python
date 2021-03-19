## install
```
npm i -D serverless-dotenv-plugin
```

## setup
create `.env` at current directory
```
LAMBDALAYER_ARN="arn:aws:lambda:<region>:<accountId>:layer:<LayerName>:<version>"
```

## Usage
### deploy
sls deploy -v --aws-profile <profile>

### execute
- get
curl https://<API GW URL> -H Authorization:<JWT>

- post
curl https://<API GW URL> -X POST -H "ContentType: application/json" -d '{ "key":"value", "key":123 }'
