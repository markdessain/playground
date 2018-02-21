# import aiohttp
# import asyncio
#
# async def fetch(session, url):
#     async with session.get(url) as response:
#         return response.status
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         status = await fetch(session, 'http://python.org')
#         print(status)
#
# ioloop = asyncio.get_event_loop()
#
# tasks = [
#     main()
#     for i in range(100)
# ]
#
# ioloop.run_until_complete(asyncio.wait(tasks))
# ioloop.close()


# import requests
# from multiprocessing import Pool
#
# def f(x):
#     print(requests.get('http://python.org').status_code)
#
# p = Pool(4)
# print(p.map(f, range(100)))

import threading
import requests

# called by each thread
def get_url():
    print(requests.get('http://python.org').status_code)

for u in range(100):
    t = threading.Thread(target=get_url)
    # t.daemon = True
    t.start()
