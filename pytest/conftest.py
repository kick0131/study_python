"""pytest.fixtureの共通参照ファイル

- ここで記載した内容は他のファイルから利用可能

"""

import pytest


@pytest.fixture(scope='module', autouse=True)
def scope_module():
    print('setup before moduleA -- conftest')
    yield(' moduleA fixture')
    print('teardown after moduleA -- conftest')


@pytest.fixture(scope='module', autouse=True)
def scope_moduleB():
    print('setup before moduleB -- conftest')
    yield(' moduleB fixture')
    print('teardown after moduleB -- conftest')


@pytest.fixture(scope='class', autouse=True)
def scope_class(scope_module, scope_moduleB):
    print('setup before class -- conftest')
    print(scope_module)
    print(scope_moduleB)
    yield(' class fixture')
    print('teardown after class -- conftest')
