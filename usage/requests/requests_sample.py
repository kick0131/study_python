import os
import requests
from logging import StreamHandler, Formatter, INFO, getLogger
from requests.exceptions import Timeout, ConnectionError, ConnectTimeout
import json
"""requestsモジュールサンプル

    aiohttp,asyncioとの比較


"""


def init_logger():
    handler = StreamHandler()
    handler.setLevel(INFO)
    handler.setFormatter(
        Formatter("[%(asctime)s] [%(threadName)s] [%(levelname)s] %(message)s"))
    logger = getLogger()
    logger.addHandler(handler)
    logger.setLevel(INFO)


def get():
    # proxyを使う場合はget(url, proxies=proxies)の形で使う
    # proxies = {
    #     "http": "http://xxxxx",
    #     "https": "http://xxxxx"
    # }
    url = 'https://api.github.com/events'
    with requests.get(url) as r:
        getLogger().info(f'url: {r.url}')
        getLogger().info(f'encoding: {r.encoding}')
        # getLogger().info(f'text:{r.text}') # データ量多いので注意


def post():
    # proxyを使う場合はpost(url, data=payload, proxies=proxies)の形で使う
    # proxies = {
    #     "http": "http://xxxxx",
    #     "https": "http://xxxxx"
    # }
    # クエリを使う場合はpost(url, params=payload)の形で使う
    url = 'http://hoge.com/post/abcde'
    payload = {'key': 'value'}
    headers = {'content-type': 'application/json'}
    with requests.post(url, data=json.dumps(payload), headers=headers) as r:
        getLogger().info(f'url: {r.url} text:{r.text}')


def file_download(url: str, path: str = './'):
    """URLからファイルをダウンロード

    Parameters
    ----------
    url : str
        ダウンロードURL
    path : str, optional
        格納先パス, by default './'

    Returns
    -------
    str
        ダウンロードファイル名
    """
    filename = url.split('/')[-1]
    filepath = os.path.join(path, filename)
    # connect timeout, read timeoutは必要
    connect_timeout = 1.0001
    read_timeout = 1.0001
    try:
        with requests.get(url, timeout=(connect_timeout, read_timeout), stream=True) as r:
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
        getLogger().info(f'filename: {filename}')
    except ConnectionError as e:
        # [connect timeout]
        # HTTPSConnectionPool(host='hira-tla2-test.s3.ap-northeast-1.amazonaws.com', port=443): Max retries exceeded with url: /helloworld.zip (Caused by ProxyError('Cannot connect to proxy.', timeout('timed out')))
        print('ConnectionError')
        getLogger().error(e)
    except ConnectTimeout as e:
        # 先にConnectionErrorが発生してしまう為、発生方法不明
        print('ConnectTimeout')
        getLogger().error(e)
    except Timeout as e:
        # [read timeout]
        # HTTPSConnectionPool(host='hira-tla2-test.s3.ap-northeast-1.amazonaws.com', port=443): Read timed out. (read timeout=0.001)
        print('Timeout')
        getLogger().error(e)
    except Exception as e:
        print('Exception')
        getLogger().error(e)

    return filename


if __name__ == "__main__":
    init_logger()

    getLogger().info('start')
    # get()
    post()
    file_url = 'https://aaa/helloworld.zip'
    # file_download(file_url)

    getLogger().info('end')
