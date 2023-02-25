#!/usr/bin/python

from concurrent.futures import ThreadPoolExecutor
import requests 

def get(url):
    result = None 

    try:
        result = requests.get(url).json()
    except requests.exceptions.ConnectionError as e:
        print(f"Failed to get {url}: {e}")

    return result

def main():
    base_url = 'https://somedomain.tld/api/v1/'
    urls = [
        base_url + 'bla/',
        base_url + 'blubb/',
        base_url + 'foo/',
        base_url + 'bar/'
    ]
    pool = ThreadPoolExecutor(max_workers=len(urls))

    for result in pool.map(get, urls):
        print(result)


if __name__ == '__main__':
    main()
