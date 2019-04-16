#!/usr/bin/python3
"""
script to search github api
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    try:
        di = r.json()
        if 'id' in di.keys():
            print(di['id'])
        else:
            print('None')
    except:
        pass
