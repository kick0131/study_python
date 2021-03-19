## Overview
API GW<br>
┗ Lambda Function -> (DataAPI) -> AuroraServerless

## First setting
- initialize
```
npm install
```

- create `.env` file
CLUSTER_ARN = "your aurora serverless ARN"
SECRET_ARN = "your secret manager ARN"


## deploy
```
sls deploy -v --aws-profile XXXXX
```

## usage
Call lambda function with query key.

ex) AWS Lambda Console Input
event = {
    "query": "select * from dummyTBL"
}

