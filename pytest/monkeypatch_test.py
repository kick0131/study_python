import test_target as target


def test_monkeypatch_setattr(monkeypatch):
    # importをしないで標準ライブラリを書き換える
    monkeypatch.setattr('platform.system', lambda: 'Linux hoge')
    result = target.get_platform()
    print(f'{result}')


def test_monkeypatch_change_const(monkeypatch):
    # 定数を書き換える
    monkeypatch.setattr(target, 'CONST_VALUE', 'after const hoge')
    result = target.CONST_VALUE
    print(f'{result}')
