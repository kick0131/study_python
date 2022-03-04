import pytest
import pytest_target


def test_mytimeout():
    """例外テスト
    """
    with pytest.raises(pytest_target.MyTimeoutError) as e:
        pytest_target.exception_sample()

    # 例外メッセージの検証
    assert str(e.value) == pytest_target.MYTIMEOUT_MESSAGE
