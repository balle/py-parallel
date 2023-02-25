#!/usr/bin/python

import multiprocessing
import requests 

def get(url):
    result = None 

    try:
        result = requests.get(url).json()
    except requests.exceptions.ConnectionError as e:
        print(f"Failed to get {url}: {e}")

    return result

def main():
    base_url = 'https://showcase.atczh.ch/api/v1/'
    urls = [
        base_url + 'employees/',
        base_url + 'sectors/',
        base_url + 'customers/',
        base_url + 'tools/',
        base_url + 'stories/'
    ]
    pool = multiprocessing.Pool(processes=len(urls))

    for result in pool.map(get, urls):
        print(result)

if __name__ == '__main__':
    main()
