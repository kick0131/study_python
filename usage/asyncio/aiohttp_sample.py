import aiohttp
import asyncio
import os
from functools import wraps
import time

from aiohttp.client import ClientSession

"""aiohttpとasyncio

    大量のhttpリクエストを捌くなら非同期モジュールであるaiohttpを使う事を検討する

    参考
    https://docs.aiohttp.org/en/stable/client_advanced.html
"""


# プロキシ
http_proxy = os.getenv('HTTP_PROXY', default=None)

GET_POKEMON_NUM = 151


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


async def get_pokemon(session: ClientSession, url: str):
    """asyncio用のポケモンゲット処理

    Parameters
    ----------
    session : ClientSession
        aiohttpクライアントセッションオブジェクト
    url : str
        ポケモンAPI取得先URL

    Returns
    -------
    str
        取得ポケモン
    """
    async with session.get(url, proxy=http_proxy) as resp:
        pokemon = await resp.json()
        return pokemon['name']


async def one_pokemon():
    async with aiohttp.ClientSession() as session:
        pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
        async with session.get(pokemon_url, proxy=http_proxy) as resp:
            pokemon = await resp.json()
            print(pokemon['name'])


async def all_pokemon():
    """非同期HTTP(aiohttp)
    """
    async with aiohttp.ClientSession() as session:
        for number in range(1, GET_POKEMON_NUM):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            async with session.get(pokemon_url, proxy=http_proxy) as resp:
                pokemon = await resp.json()
                print(pokemon['name'])


async def all_pokemon_asyncio():
    """非同期HTTP(aiohttp)とコルーチン(asyncio)
    """
    async with aiohttp.ClientSession() as session:
        tasks = []
        for number in range(1, GET_POKEMON_NUM):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.ensure_future(
                get_pokemon(session, pokemon_url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)


@stop_watch
def main():
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(all_pokemon())  # 8.58秒
    loop.run_until_complete(all_pokemon_asyncio())  # 1.61秒


if __name__ == "__main__":
    main()
