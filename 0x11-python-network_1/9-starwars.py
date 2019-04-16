#!/usr/bin/python3
"""
script to search starwars api
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://swapi.co/api/people/?search='
    if len(sys.argv) > 1:
        url += sys.argv[1]
    r = requests.get(url)
    try:
        di = r.json()
        if di:
            print('Number of results: {}'.format(di['count']))
            for i in di['results']:
                print(i['name'])
    except ValueError:
        print('Not a valid JSON')
