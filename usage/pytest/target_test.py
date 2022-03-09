import pytest
import target


def test_getenv(setupEnv):
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


@pytest.mark.skip
def test_not_action():
    """テスト対象外にするアノテーション
    """
    assert True


@pytest.mark.parametrize(
    "x, y, expect", [
        (0, 1, 1),
        (2, 2, 4),
        (3, 4, 7)
    ]
)
def test_parametrize(x, y, expect):
    """引数のパターンチェック
    """

    assert target.plus(x, y) == expect
