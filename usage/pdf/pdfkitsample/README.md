# pdf作成
pythonでテキスト検索できるPDFの作り方を調査

## setup

### [wkhtmltopdfのダウンロード](https://wkhtmltopdf.org/downloads.html)
windowsの場合、実行ファイルを適当なパスに配置

### .envファイルを用意
```bash
PROXY="プロキシ"
WKHTMLTOPDF_PATH="wkhtmltopdf.exeまでのファイルパス"
```
### 実行
```bash
python usage.py
```

## 参考
[参考1](https://qiita.com/danishi/items/e9e0d5c1a8dae1f99b40)

[参考2](https://qiita.com/morita-toyscreation/items/1f90724a797f1b63a9c9)
