from functools import wraps
import concurrent
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
from logging import StreamHandler, Formatter, INFO, getLogger

"""ThreadPoolExecutor、ProcessPoolExecutor実装サンプル

    どちらも生成コストがかかるので短い処理には向いていない
    IFはほぼ共通なので、一部オプション(thread_name_prefix)を除き、
    クラスの差し替えのみで切替可能
    max_workersオプションでワーカー数(スレッド、プロセス)上限を定義

    [ProcessPoolExecutor]
    子プロセスを生成するので親プロセスの処理(init_logger)が反映されない
    生成コストが高いので、スレッドとの比較は注意。
    現に、このサンプルプログラムはスレッドの方が早い。

    submit(),map()の違いは呼び出し方と戻り値の型が異なる。
    「どのタスク」を「どの引数で実行するか」という部分は同じ。

    アムダールの法則(並列化できない部分が性能限界になる)に従う

    CPython(C言語で実装されたPython)ではGIL(Global Interpreter Lock)の制約を受け、
    複数スレッド存在しても、常に排他処理によって単一スレッドで動作する。

    参考
    https://qiita.com/ttiger55/items/5e1d5a3405d2b3ef8f40

"""
# ワーカー上限
MAX_WORKER = 10

# タイムアウト秒
WORKER_TIMEOUT = 10

# タスクに渡す引数リスト
# 並列で実行する場合、処理時間の短縮度合いを比較
args = [
    {
        'id': 'value1',
        'timer': 2
    },
    {
        'id': 'value2',
        'timer': 2
    },
    {
        'id': 'value3',
        'timer': 2
    },
    {
        'id': 'value4',
        'timer': 2
    },
    {
        'id': 'value5',
        'timer': 2
    },
]


def stop_watch(func):
    """処理時間計測用のデコレータ
    """
    @wraps(func)
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        elapsed_time = time.time() - start
        print(f"{func.__name__}は{elapsed_time}秒かかりました")
        return result
    return wrapper


def init_logger():
    """ロガー初期化

    初期化後、getLogger().info('hello')の様に使う

    """
    handler = StreamHandler()
    handler.setLevel(INFO)
    handler.setFormatter(
        Formatter("[%(asctime)s] [%(threadName)s] %(message)s"))
    logger = getLogger()
    logger.addHandler(handler)
    logger.setLevel(INFO)


class MainTask:
    """タスククラス

    callableオブジェクトにすることでクラスインスタンスを直接
    executerに指定できる。

    """

    def __init__(self):
        # マルチスレッドだとアリだが、マルチプロセスだとナシ
        init_logger()

    def __call__(self, task_val, timer=0):
        """タスクメイン処理

        Parameters
        ----------
        task_val : any
            No use
        timer : int, optional
            additional sleep timer, by default 0
        """
        getLogger().info(f'{task_val} start')
        self._xxx()
        time.sleep(1.0 + timer)
        getLogger().info(f'{task_val} end')
        return task_val

    def _xxx(self):
        """処理A

        タスクメインから呼び出される処理は個別にメソッド定義

        """
        pass


@stop_watch
def multithread_with_submit():
    """submitを使ったマルチスレッド

    submitの戻り値はFuture型
    Futureオブジェクトを使い、実行中スレッドの操作(待機、中断)が可能

    """

    with ThreadPoolExecutor(max_workers=MAX_WORKER, thread_name_prefix='thread') as executor:
        futures = []
        mytask = MainTask()

        getLogger().info('-- multithread ready --')

        # スレッド即時に応答し、実行結果格納オブジェクト(Future)を受け取る
        futures = [executor.submit(
            mytask, arg['id'], timer=arg['timer']) for arg in args]
        try:
            # 完了まで待機、timeoutの単位は秒
            for future in concurrent.futures.as_completed(futures, timeout=WORKER_TIMEOUT):
                # スレッド完了まで同期
                getLogger().info(f'result : {future.result()}')

            else:
                print('All thread Done')

        except concurrent.futures.thread.BrokenThreadPool as a:
            print('BrokenThreadPool')
            getLogger().error(f'err: {a}')

        except concurrent.futures.TimeoutError as a:
            print('TimeoutError')
            getLogger().error(f'err: {a}')

        except Exception as a:
            print('Exception')
            getLogger().error(f'err: {a}')

        getLogger().info('-- multithread Done --')


def multithread_with_map():
    """mapを使ったマルチスレッド

    map(task, arg)
    第2引数argはIterableな値とする必要がある

    戻り値はIterator型

    """
    mytask = MainTask()

    getLogger().info('main start')
    with ThreadPoolExecutor(max_workers=2, thread_name_prefix='thread') as executor:
        results = executor.map(mytask, range(2))
        getLogger().info('map end')
    getLogger().info(list(results))
    getLogger().info('main end')


@stop_watch
def multiprocess_with_submit():
    """submitを使ったマルチプロセス

    submitの戻り値はFuture型
    Futureオブジェクトを使い、実行中スレッドの操作(待機、中断)が可能

    """
    mytask = MainTask()

    with ProcessPoolExecutor(max_workers=MAX_WORKER) as executor:
        futures = []

        getLogger().info('-- multiprocess ready --')

        # スレッド即時に応答し、実行結果格納オブジェクト(Future)を受け取る
        futures = [executor.submit(
            mytask, arg['id'], timer=arg['timer']) for arg in args]
        try:
            # 完了まで待機、timeoutの単位は秒
            for future in concurrent.futures.as_completed(futures, timeout=WORKER_TIMEOUT):
                # スレッド完了まで同期
                getLogger().info(f'result : {future.result()}')

            else:
                print('All thread Done')

        except concurrent.futures.thread.BrokenThreadPool as a:
            print('BrokenThreadPool')
            getLogger().error(f'err: {a}')

        except concurrent.futures.TimeoutError as a:
            print('TimeoutError')
            getLogger().error(f'err: {a}')

        except Exception as a:
            print('Exception')
            getLogger().error(f'err: {a}')

        getLogger().info('-- multiprocess Done --')


if __name__ == "__main__":
    # multithread_with_map()
    # multithread_with_submit()
    multiprocess_with_submit()
