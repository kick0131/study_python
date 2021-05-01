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

## 実行例
- コマンドプロンプト

    `curl -X POST -H "Content-Type: application/json" -d "{\"key\":\"value\"}" http://localhost:5000/post/ABCDE`

## pytest

    `pytest -s .\usage\flask\test_app.py`

