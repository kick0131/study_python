# Description

# Prepare
### テーブルを作成する
コンソールやCLIなど  
最低限テーブル名とパーティションキーがあれば良い

### aws/.envファイルを作成し、以下環境変数を定義する
- AWS_PROFILE
- DYNAMODB_TABLE

※aws.myenvモジュールが.envを読み込み、aws.myenvを利用して間接的に環境変数を取り込んでいる

