"""pytest.fixtureの共通参照ファイル

- ここで記載した内容は他のファイルから利用可能

"""
import pytest
import target

@pytest.fixture(scope='session', autouse=True)
def setupEnv():
    """MonkeyPatchを使った環境変数の書き換え例

    例えばテスト対象のモジュールがグローバルスコープで環境変数を取得していたとする
    region = os.getenv('AWS_REGION')

    テスト対象がimportでそのモジュールを読み込むと、テスト関数を呼ぶ前に
    os.getenvが呼ばれてしまい、setupで環境変数を書き換えても遅い。

    この場合、環境変数ではなく、読み込み先変数(例の場合region)を書き換える事で
    間接的に環境変数を書き換える事が実現できる。

    """
    mp = pytest.MonkeyPatch()
    mp.setattr(target, 'region', 'ap-northeast-1')


@pytest.fixture(scope='module', autouse=True)
def conftext_moduleA():
    print('setup before ---- conftext_moduleA')
    yield(' yield conftext_moduleA')
    print('teardown after -- conftext_moduleA')


@pytest.fixture(scope='module', autouse=True)
def conftext_moduleB():
    print('setup before ---- conftext_moduleB')
    yield(' yield conftext_moduleB')
    print('teardown after -- conftext_moduleB')


@pytest.fixture(scope='class', autouse=True)
def constest_class(conftext_moduleA, conftext_moduleB):
    print('setup before ---- constest_class')
    print(conftext_moduleA)
    print(conftext_moduleB)
    yield(' yield constest_class')
    print('teardown after -- constest_class')
