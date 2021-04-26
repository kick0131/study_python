
def test_always_scceeds(scope_class):
    print('=== test_always_scceeds')
    print(scope_class)
    assert True


class TestClass():
    def test_always_succeeds_under_class(self, scope_module):
        print(f'=== {__name__}')
        print(scope_module)
        assert True
