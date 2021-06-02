from usage.flask.api import app
"""ファイル分割サンプル
"""


@app.route('/hello')
def helloworld():
    return 'Hello World'
