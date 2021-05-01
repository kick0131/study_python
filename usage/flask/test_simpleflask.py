import pytest
import flask
from usage.flask.simpleflask import app


@pytest.fixture(scope='function', autouse=True)
def dummy():
    print('setup before')
    yield(' functionA fixture')
    print('teardown after')


def test_post_form(dummy):
    """Form画面を想定したリクエスト

    以下のやり方はNG、Flaskからのマッピングができない
    simpleflask.post('aaa')

    """
    # flaskのテストモード有効
    app.config['TESTING'] = True

    # flaskクライアント
    client = app.test_client()

    # flaskクライアントを使って対象のルーティングを呼び出す
    # dictでフォームパラメータ指定
    result = client.post('/post/ABCDE', data=dict(
        username='taro',
        password='t@ro'
    ))
    print(f'client result : {result}')

    with app.test_request_context('/post'):
        # Flaskが呼ばれたリクエストパスの確認
        print(f'flask.request.path : {flask.request.path}')
        print(f'flask.request.args : {flask.request.args}')

    assert True


def test_post_json(dummy):
    """application/jsonでのRESTAPI実行サンプル
    """
    # flaskのテストモード有効
    app.config['TESTING'] = True

    # flaskクライアント
    client = app.test_client()

    # flaskクライアントを使って対象のルーティングを呼び出す
    # jsonでリクエストボディ指定
    result = client.post('/post/ABCDE', json={
        'email': 'taro@gmail.com',
        'password': 'Gm@i1.com'
    })
    print(f'client result : {result}')

    with app.test_request_context('/post'):
        # Flaskが呼ばれたリクエストパスの確認
        print(f'flask.request.path : {flask.request.path}')
        print(f'flask.request.args : {flask.request.args}')

    assert True
