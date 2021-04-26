import pytest

# セットアップ関連をこのファイルに集約


@pytest.fixture(scope='module', autouse=True)
def scope_module():
    print('setup before moduleA')
    yield(' moduleA fixture')
    print('teardown after moduleA')


@pytest.fixture(scope='module', autouse=True)
def scope_moduleB():
    print('setup before moduleB')
    yield(' moduleB fixture')
    print('teardown after moduleB')


@pytest.fixture(scope='class', autouse=True)
def scope_class(scope_module, scope_moduleB):
    print('setup before class')
    print(scope_module)
    print(scope_moduleB)
    yield(' class fixture')
    print('teardown after class')
