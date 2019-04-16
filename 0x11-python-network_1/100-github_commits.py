#!/usr/bin/python3
"""
script to search github api
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/repos/' + sys.argv[2] + '/'
    url += sys.argv[1] + '/commits'
    r = requests.get(url)
    try:
        di = r.json()
        for i in range(10):
            print('{}: {}'.format(
                di[i]['sha'], di[i]['commit']['committer']['name']))
    except:
        pass
