pytest sample
===

## pip
```
pipenv install --dev pytest pytest-cov pytest-mock
```

## Test
- コンソール出力

  `pytest -s <testpath>`

- テスト＋カバレッジ

  `pytest -v --cov=api --cov-report=term-missing <testpath>`

- HTML出力(htmlcovに出力)

  `pytest -v --cov=api --cov-report=html <testpath>`


## 注意点

- conftest.pyはpytestが参照する固定ファイル名

