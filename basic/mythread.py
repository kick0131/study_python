import concurrent
from concurrent.futures import ThreadPoolExecutor
import time
from logging import StreamHandler, Formatter, INFO, getLogger

"""ThreadPoolExecutorでスレッドプールを用意し、スレッド上限を定義
"""


def init_logger():
    handler = StreamHandler()
    handler.setLevel(INFO)
    handler.setFormatter(
        Formatter("[%(asctime)s] [%(threadName)s] %(message)s"))
    logger = getLogger()
    logger.addHandler(handler)
    logger.setLevel(INFO)


def task(task_val, timer=0):
    """スレッド実行タスク

    Parameters
    ----------
    task_val : any
        No use
    timer : int, optional
        additional sleep timer, by default 0

    Returns
    -------
    any
        echo task_val
    """

    getLogger().info(f'{task_val} start')
    time.sleep(1.0 + timer)
    getLogger().info(f'{task_val} end')
    return task_val


def multithread_with_submit():
    """submitを使ったマルチスレッド

    submitの戻り値はFuture型
    Futureオブジェクトを使い、実行中スレッドの操作(待機、中断)が可能

    """
    init_logger()

    with ThreadPoolExecutor(max_workers=3, thread_name_prefix='thread') as executor:
        futures = []

        getLogger().info('-- ready --')
        # タスクに渡す引数リスト
        args = [
            # 正常終了
            {
                'id': 'value1',
                'timer': 1
            },
            # タイムアウトを期待
            {
                'id': 'value2',
                'timer': 3
            },
        ]

        # スレッド即時に応答し、実行結果格納オブジェクト(Future)を受け取る
        futures = [executor.submit(
            task, arg['id'], timer=arg['timer']) for arg in args]
        try:
            # 完了まで待機、timeoutの単位は秒
            for future in concurrent.futures.as_completed(futures, timeout=3):
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

        getLogger().info('-- Done --')


def multithread_with_map():
    """mapを使ったマルチスレッド

    map(task, arg)
    第2引数argはIterableな値とする必要がある

    戻り値は

    """
    init_logger()
    getLogger().info('main start')
    with ThreadPoolExecutor(max_workers=2, thread_name_prefix='thread') as executor:
        results = executor.map(task, range(2))
        getLogger().info('map end')
    getLogger().info(list(results))
    getLogger().info('main end')


if __name__ == "__main__":
    # multithread_with_map()
    multithread_with_submit()
