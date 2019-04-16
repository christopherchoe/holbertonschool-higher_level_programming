#!/usr/bin/python3
"""
script to takes url and display body of response to request
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPErro as e:
        print('Error code: {}'.format(e.code))
