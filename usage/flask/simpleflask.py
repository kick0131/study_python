"""Flaskシンプルアプリ
"""
from flask import request, redirect, url_for, jsonify
import random
from basic.logutil.mylogging_helper import createDeveloplogger
from usage.flask.api import app

# ロガー
logger = createDeveloplogger(__name__, 'log/debug.log')


def picked_up():
    """メッセージをランダムに変換
    """
    messages = [
        "こんにちは、あなたの名前を入力してください",
        "やあ！お名前は何ですか？",
        "あなたの名前を教えてね"
    ]
    return messages[random.randint(1, 3)]


@app.route('/')
def index():
    return jsonify({
        'before': 'testdata',
        'after ': 'randdata'
    })


@app.route('/post/<pathparam>', methods=['GET', 'POST'])
def post(pathparam):

    logger.info(f'== パスパラメータ: {pathparam}')
    logger.info(f'== リクエストヘッダ: {request.headers}')
    logger.info(f'== HTTPメソッド {request.method}')

    if request.method == 'POST':
        logger.info(f'リクエストフォーム(raw) : {request.form}')
        # ImmutableMultiDict -> dict変換
        formdata = request.form.to_dict()
        logger.info(f'リクエストフォーム(dict): {formdata}')

        logger.info(f'is_json: {request.is_json}')
        if request.is_json is not None:
            logger.info(f'リクエストボディ:{request.get_json()}')

        return jsonify({
            'before': 'testdata',
            'after ': 'randdata'
        })

    else:
        # リダイレクト
        return redirect(url_for('index'))


if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0')
