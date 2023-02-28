import time
from pathlib import Path
from typing import Callable

import httpx
from concurrent import futures

POP20_CC = ('CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'https://www.fluentpython.com/data/flags'
DEST_DIR = Path('downloaded')


def save_flag(img: bytes, filename: str) -> None:
    (DEST_DIR / filename).write_bytes(img)


def get_flat(cc: str) -> bytes:
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    resp = httpx.get(url, timeout=5.1, follow_redirects=True)
    resp.raise_for_status()
    return resp.content


def download_one(cc: str):
    image = get_flat(cc)
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)


# def download_many(cc_list: list[str]) -> int:
#     for cc in sorted(cc_list):
#         image = get_flat(cc)
#         save_flag(image, f'{cc}.gif')
#         print(cc, end=' ', flush=True)
#     return len(cc_list)

def download_many(cc_list: list[str]) -> int:
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor() as executor:
        to_do: list[futures.Future] = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            print(f'Scheduled for {cc}: {future}')

        for count, future in enumerate(futures.as_completed(to_do), 1):
            res: str = future.result()
            print(f'{future} result: {res!r}')
    return count


# def main(downloader: Callable[[list[str]], int]) -> None:
#     DEST_DIR.mkdir(exist_ok=True)
#     t0 = time.perf_counter()
#     count = downloader(POP20_CC)
#     elapsed = time.perf_counter() - t0
#     print(f'\n{count} downloads in {elapsed:.2f}s')

from time import sleep, strftime
from concurrent import futures

def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)

def loiter(n):
    msg = '{}liter({}): doing nothing for {}s...'
    display(msg.format('\t'*n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t'*n, n))
    return n*10

def main():
    display('Script has stated.')
    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, range(5))
    display('results:', results)


if __name__ == '__main__':
    main()
