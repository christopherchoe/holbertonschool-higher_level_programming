#!/usr/bin/python3
"""
script to takes url and display body of response to request
"""
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        if r.status_code == 200:
            print(r.text)
        else:
            print('Error code: {}'.format(r.status_code))
    except:
        pass
