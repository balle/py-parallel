#!/usr/bin/python

import asyncio
import requests 

async def get(url):
    try:
        print(requests.get(url).json()) 
    except requests.exceptions.ConnectionError as e:
        print(f"Failed to get {url}: {e}")
    #await asyncio.sleep(1)

async def main():
    base_url = 'https://somedomain.tld/api/v1/'
    urls = [
        base_url + 'bla/',
        base_url + 'blubb/',
        base_url + 'foo/',
        base_url + 'bar/'
    ]
    tasks = []

    for url in urls:
        tasks.append(loop.create_task(get(url)))

    await asyncio.wait(tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
