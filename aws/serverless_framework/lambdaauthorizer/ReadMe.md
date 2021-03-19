## Overview
API GW<br>
┣ Lambda Authorizer -> (CognitoAPI) -> Cognito<br>
┃┗ Lambda Layer(OSS Liblary)<br>
┗ Lambda Function<br>

## before setup(aleady done)
- Download LambdaLayer program file
download OSS file to local `<yourname>` directory
```
curl -O https://raw.githubusercontent.com/awslabs/aws-support-tools/master/Cognito/decode-verify-jwt/decode-verify-jwt.py
```

- rename pythonfile(default file name is PEP8 error)

- mkdir `python` directory for lambdalayer
- put in OSS file and required files
```
cd python
pip install -t ./ python-jose
```

## setup
create `.env` at current directory
```
LAMBDALAYER_ARN="arn:aws:lambda:<region>:<accountId>:layer:<LayerName>:<version>"
```

### sample JWT
eyJraWQiOiJ6V2ZDODFGdjBWcWZCRVhKU3R6SHlCaHQxTklnV1VtejZkdDdnc25RaFBZPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJkYWFhYzZkZS03ZDUzLTQ0NGItOTZhNC1mYzhjM2Q2ODY0NGUiLCJhdWQiOiI1cjBzdGpvYmJvdDF2cGw5OHNiNzE1MTl1bSIsImV2ZW50X2lkIjoiZjIyOGQxODYtNWVjMS00NzlhLWFhOWEtZjU4MTA3MzUyYzQyIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE1OTQ5ODgwMjYsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1ub3J0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1ub3J0aGVhc3QtMV80WTVRS0dsNzUiLCJjb2duaXRvOnVzZXJuYW1lIjoidGVzdHVzZXJAbWFpbC5jb20iLCJleHAiOjE1OTQ5OTE2MjYsImlhdCI6MTU5NDk4ODAyNywiZW1haWwiOiJ0ZXN0dXNlckBtYWlsLmNvbSJ9.cgOOjniLfUg5Bv8br0SnLk05LdiwD01MZumxw0sM_hl9ZWs4rznehwawTSeJRjWeem2RCkzvh2SJ2E__6ysnaBP0O8V6JC65rMLS5cs3XlFqcph-sWllXmDLYKZIzfLMgLtBIIomMkSRRko01dxoMISDqhcBf2IOd0ZwY0xtihBQ4lLpbuWKllR3AYL_pGYfLgfSN1XPnxAqJ-BC9qpHaxeuEXLpLejO8DfFYKrEee0hRHp_fowoG76xI4T3LAQEu2r2M4KC7D2n7vKPm_e8_R9lOm9z8S3mt-sYNSu8RJ34-CFvw5hEmqPU3FBAUPX5Z1zfGWfcGZzM0KtrxsOa-


## Usage
### deploy
sls deploy -v --aws-profile <profile>

### execute
- get
curl https://<API GW URL> -H Authorization:<JWT>

- post
curl https://<API GW URL> -X POST -H "ContentType: application/json" -d '{ "key":"value", "key":123 }'
