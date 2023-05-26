# import time
#
#
# def foo():
#     print('One')
#     time.sleep(1)
#     print('Two')
import asyncio
import threading
# start = time.time()
#
# for _ in range(3):
#     foo()
#
# print(f'Took: {time.time() - start}')

# import asyncio
#
#
# async def foo_async():
#     print('One')
#     await asyncio.sleep(1)
#     print('Two')
#
#
# async def main():
#     await asyncio.gather(foo_async(), foo_async(), foo_async())
#
#
# start = time.time()
# asyncio.run(main())  # event loop
# print(f'Took: {time.time() - start}')

# def foo_generator():
#     for i in range(3):
#         print('1')
#         yield i
#
#
# for j in foo_generator():
#     print('2')

import time

import httpx
import requests

# urls = [
#     'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
#     'https://wiki.nazk.gov.ua/',
#     'https://commons.wikimedia.org/wiki/Main_Page'
# ] * 20

# start = time.time()
#
#
# def foo(url_):
#     response = requests.get(url_)
#     print(response.status_code)
#
#
# for url in urls:
#     foo(url)
#
#
# print(f'Execution: {time.time() - start}')


# start = time.time()
#
#
# def foo_threading(url_):
#     response = requests.get(url_)
#     print(response.status_code)
#
#
# threads = []
#
# for url in urls:
#     th1 = threading.Thread(target=foo_threading, args=[url])
#     threads.append(th1)
#     th1.start()
#
# for th in threads:
#     th.join()
#
#
# print(f'Execution: {time.time() - start}')

urls = [
    'http://localhost:8000',
] * 60


async def foo_async(url_: str) -> None:
    # response = requests.get(url_)
    async with httpx.AsyncClient() as client:
        response = await client.get(url_, timeout=30)
    print(response.status_code)


async def main():
    tasks = []

    for url in urls:
        tasks.append(foo_async(url))

    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
print(f'Execution: {time.time() - start}')
