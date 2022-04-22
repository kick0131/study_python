import pdfkit

# .envファイルから環境変数を取得
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

PROXY = os.environ.get("PROXY")
WKHTMLTOPDF_PATH = os.environ.get("WKHTMLTOPDF_PATH")
print(WKHTMLTOPDF_PATH)


# 指定できる出力オプション https://wkhtmltopdf.org/usage/wkhtmltopdf.txt
options = {
    'page-size': 'A4',
    'margin-top': '0.1in',
    'margin-right': '0.1in',
    'margin-bottom': '0.1in',
    'margin-left': '0.1in',
    'encoding': "UTF-8",
    'no-outline': None,
    'disable-smart-shrinking': '',
    '--proxy': PROXY,
}

# WebページをPDF出力
#pdfkit.from_url('https://google.com', 'google.pdf', options=options)

# パスを通さなかった場合はプログラム内でパスを設定する必要がある。
config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
pdfkit.from_url('https://google.com', 'google.pdf',
                options=options, configuration=config)

# HTML/CSSファイルをPDF出力
#pdfkit.from_file('index.html', 'index.pdf', css='style.css', options=options)

# テキストをPDF出力
#pdfkit.from_string('<html><body><h1>It works!</h1></body></html>', 'apache.pdf', options=options)
