## 概要
Flaskアプリケーションのテスト

目的
- 単体テストの実行方法の理解
- @routeで渡されるパラメータの編集方法 

お題
- HTTPリクエストに対して元の文字とランダムで文字列を並び替えた文字をjson形式で返すRESTAPI

## 準備
```
pipenv install flask
```

## Flaskアプリの起動

`python usage/flask/simpleflask.py  `

- api/__init__.pyでFlaskアプリを生成し、他のモジュールをimportすることでファイル分割を可能としている

## 実行例
- コマンドプロンプト

    `curl -X POST -H "Content-Type: application/json" -d "{\"key\":\"value\"}" http://localhost:5000/post/ABCDE`

- ブラウザからアクセス
    `http://localhost:5000/<API>`

## pytest

    `pytest -s .\usage\flask\test_simpleflask.py`

