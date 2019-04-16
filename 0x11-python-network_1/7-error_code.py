#!/usr/bin/python3
"""
script to takes url and display body of response to request
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.raise_for_status == requests.codes.ok:
        print(r.text)
    else:
        print('Error code: {}'.format(r.status_code))
