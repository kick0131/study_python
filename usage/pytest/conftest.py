"""pytest.fixtureの共通参照ファイル

- ここで記載した内容は他のファイルから利用可能

"""

import pytest


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
