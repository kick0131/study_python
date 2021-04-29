"""loggerの継承関係を理解するためのpytest

https://qiita.com/Kept1994/items/ae2853addb64fdda9139

"""
import basic.logutil.client_a as client_a
import basic.logutil.client_b as client_b

# ルートロガーの操作は子供に影響するから厳禁!!!
# logger = propagate.getlogger()


def test_sample01():
    """それぞれのモジュールからロガーの生成とログ呼び出しを実行
    """
    print('')
    # root
    # - top (handler)
    # logger名が同じなのでハンドラが重複して登録される
    # ⭐️なので、__name__でロガーを作った方が良い
    client_a.calltop()
    # 同じロガー名なのでhandler +1
    client_b.calltop()

    # --------------------------------------------
    # logger.propagate
    # logger.propagateの値を書き換えて出力結果を確認する
    # True  : topのハンドラにも渡される
    # False : topのハンドラに渡されない
    # --------------------------------------------
    # root
    # - top (handler)
    # --  sub1 (handler)
    client_a.callsub1()
    client_b.callsub1()
    # root
    # - top (handler)
    # --  sub2 (handler)
    client_a.callsub2()
    client_b.callsub2()
