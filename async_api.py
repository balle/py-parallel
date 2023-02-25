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
    base_url = 'https://showcase.atczh.ch/api/v1/'
    urls = [
        base_url + 'employees/',
        base_url + 'sectors/',
        base_url + 'customers/',
        base_url + 'tools/',
        base_url + 'stories/'
    ]
    tasks = []

    for url in urls:
        tasks.append(loop.create_task(get(url)))

    await asyncio.wait(tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
