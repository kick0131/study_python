import pprint
import traceback


class ParentException(Exception):
    """例外クラス
    """
    code = ''

    def __init__(self):
        self.code = 'parParentExceptionent'

    def __str__(self):
        return '{} is Occured'.format(self.code)


class P_ParentException(ParentException):
    """例外クラス
    """

    def __init__(self):
        self.code = 'P_ParentException'

    def __str__(self):
        return '{} is Occured'.format(self.code)


def sampleRun():
    """サンプル関数
    """
    result = 'success'

    try:
        #        1/0 # ZeroDivisionError Trigger
        #        raise P_ParentException()
        raise Exception()

    # 例外オブジェクトを補足
    except ZeroDivisionError as errorObject:
        pprint.pprint('== ZeroDivisionError reason:{}'.format(errorObject))
        result = 'Error'

    # 複数オブジェクトをまとめて補足
    except (ParentException, P_ParentException) as errorObject:
        pprint.pprint('== ZeroDivisionError reason:{}'.format(errorObject))
        result = 'Error'

    # とにかく補足
    except:
        # スタックトレースは出すべき
        pprint.pprint('== Error occured reason:{}'.format(
            traceback.format_exc()))
        result = 'Error'

    else:   # 正常終了 本来やりたい事
        pprint.pprint(result)

    finally:  # 強制実行 どうしてもやる必要のある事
        pass  # 何もしない場合の構文

    return result


if __name__ == '__main__':
    print("{0}".format(sampleRun()))
