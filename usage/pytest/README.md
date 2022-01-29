pytest sample
===

## Basic rule

- `test_`から始まるメソッドがテスト対象
- conftest.pyはpytestがfixutureとして参照する固定ファイル

## setup
```
pipenv install --dev pytest pytest-cov pytest-mock
```

## Let's start
```bash
# コンソール出力
# ex) pytest -s ./pytest/
pytest -s <testpath>

# メソッド名に一致するテストを指定して実行
# ex) pytest -v -k monkeypatch .
pytest -k <search> <testpath>

# カバレッジ出力(コンソール)
# ex) pytest -v --cov=. --cov-report=term-missing .
pytest -v --cov=<testpath> --cov-report=term-missing <testpath>

# カバレッジ出力(html)
# ex) pytest -v --cov=. --cov-report=html .
pytest -v --cov=<testpath> --cov-report=html <testpath>
```

### オプション
|オプション|意味|
|--|--|
|-v|詳細出力|
|-s|コンソール出力|
|-k|メソッド名検索|
|--cov| カバレッジON ※要pytest-covライブラリ |
|--cov-report| カバレッジ結果出力フォーマットの指定 |



