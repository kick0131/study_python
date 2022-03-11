"""Fixtureのスコープを確認するサンプル
- fixtureは引数に渡す渡さないに関わらず、スコープに応じて必ず実行される
- fixtureで生成したオブジェクトを使用する場合はテストメソッドの引数として渡す
- yieldを使うと「メソッドの最初」「メソッド終了時」に処理を分けられる
- class : クラス単位で1回のみ実行

"""
import sys
import pytest


@pytest.fixture(scope='function', autouse=True)
def scope_functionA():
    print('setup before ---- scope_functionA')
    yield(' functionA fixture')
    print('teardown after -- scope_functionA')


@pytest.fixture(scope='function', autouse=True)
def scope_functionB():
    print('setup before ---- scope_functionB')
    yield(' functionB fixture')
    print('teardown after -- scope_functionB')


@pytest.fixture(scope='module', autouse=True)
def scope_moduleA():
    print('setup before ---- scope_moduleA')
    yield(' moduleA fixture')
    print('teardown after -- scope_moduleA')


@pytest.fixture(scope='module', autouse=True)
def scope_moduleB():
    print('setup before ---- scope_moduleB')
    yield(' moduleB fixture')
    print('teardown after -- scope_moduleB')


@pytest.fixture(scope='class', autouse=True)
def scope_class(conftext_moduleA, scope_moduleB):
    print('setup before ---- scope_class')
    yield(' class fixture')
    print('teardown after -- scope_class')


def test_always_success():
    print('=== test_always_success')
    assert True


class TestClassA():
    def test_classA_moduleA(
            self, scope_class, scope_functionA, scope_moduleA,
            scope_functionB, scope_moduleB):
        print(f'=== {sys._getframe().f_code.co_name}')
        assert True

    def test_classA_moduleB(
            self, scope_class, scope_functionA, scope_moduleA,
            scope_functionB, scope_moduleB):
        print(f'=== {sys._getframe().f_code.co_name}')
        assert True


class TestClassB():
    def test_classB_moduleA(
            self, scope_class, scope_functionA, scope_moduleA,
            scope_functionB, scope_moduleB):
        print(f'=== {sys._getframe().f_code.co_name}')
        assert True

    def test_classB_moduleB(
            self, scope_class, scope_functionA, scope_moduleA,
            scope_functionB, scope_moduleB):
        print(f'=== {sys._getframe().f_code.co_name}')
        assert True
