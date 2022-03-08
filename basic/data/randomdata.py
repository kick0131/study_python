import random
import string


def randomstr(datalen: int) -> str:
    """ランダム文字列を生成する

    ASCIIと数字

    Args:
        datalen (int): 生成する文字数

    Returns:
        str: ランダム文字列
    """
    return ''.join(random.SystemRandom().choice(
        string.ascii_letters + string.digits)
        for _ in range(datalen))


if __name__ == '__main__':
    print(f'{randomstr(20)}')
