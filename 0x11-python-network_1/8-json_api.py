#!/usr/bin/python3
"""
script to takes url and sends post request with input letter
"""
import requests
import sys


if __name__ == "__main__":
    param = {'q': ""}
    if len(sys.argv) > 1:
        param['q'] = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data=param)
    try:
        if r.json():
            print('[{}] {}'.format(r.json()['id'], r.json()['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
