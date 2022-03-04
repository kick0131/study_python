import pytest
import target


def testGetEnv(setupEnv):
    """環境変数の書き換え

    詳細はconftest.pyを参照
    """
    assert target.get_env() == 'ap-northeast-1'


def test_mytimeout():
    """例外テスト
    """
    with pytest.raises(target.MyTimeoutError) as e:
        target.exception_sample()

    # 例外メッセージの検証
    assert str(e.value) == target.MYTIMEOUT_MESSAGE
