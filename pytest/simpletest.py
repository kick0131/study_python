import pytest


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


def test_always_scceeds(scope_class):
    print('=== test_always_scceeds')
    print(scope_class)
    assert True


class TestClass():
    def test_always_succeeds_under_class(self, scope_module):
        print(f'=== {__name__}')
        print(scope_module)
        assert True
