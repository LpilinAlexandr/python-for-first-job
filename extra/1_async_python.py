"""
Работа с асинхронным python
"""
import asyncio
import time

import aiohttp
import requests


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


URLS = [
    'https://google.com',
    'https://www.youtube.com/',
    'https://www.djangoproject.com/',
    'https://www.python.org/',
    'https://www.wikipedia.org/'
]


def time_tracker(func):
    """Декоратор для измерения скорости работы декорируемой функции."""

    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time() - start

        print(f'Функция {func.__name__} отработала за {end} секунд.')

    return wrapper


async def make_async_request(idx, url, session: aiohttp.ClientSession) -> None:
    """Асинхронный запрос на url."""
    async with session.get(url) as response:
        if 200 <= response.status < 300:
            text = 'успешно'
        else:
            text = 'безуспешно'

        print(f'{idx} | {url}: {text}', end='\n')


def make_sync_request(idx, url) -> None:
    """Синхронный запрос на url."""
    response = requests.get(url)
    if 200 <= response.status_code < 300:
        text = 'успешно'
    else:
        text = 'безуспешно'

    print(f'{idx} | {url}: {text}', end='\n')


async def async_run(count: int) -> None:
    """Отправить N асинхронных запросов."""
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(count):
            tasks.append(make_async_request(idx=i, url=URLS[i % len(URLS)], session=session))

        await asyncio.gather(*tasks)


def sync_run(count: int) -> None:
    """Отправить N синхронных запросов."""
    for i in range(count):
        make_sync_request(idx=i, url=URLS[i % len(URLS)])


@time_tracker
def async_main() -> None:
    asyncio.run(async_run(1000))


@time_tracker
def sync_main() -> None:
    sync_run(30)


if __name__ == '__main__':
    async_main()
    sync_main()
