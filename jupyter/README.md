# Jupyter

## カーネルをpipenvの環境に変更
(引用)https://qiita.com/mzn/items/99d769d0ad9d03a5d73e
```
pipenv shell
python -m ipykernel install --user --name=<お好きな名前>
```
jupyter接続後、インタープリタをpipenv環境のpythonに指定

## 実行方法
1. (vscodeとは別のターミナルで実行)pipenv環境（Jupyterインストール済）で以下コマンドを実行
    ```
    jupyter lab
    ```
    Jupyterが起動し、自動でブラウザからJupyterにアクセスする

2. notebookを開き、右上のJupyterServerから手順１で立ち上げたJupyterServerを選択する

