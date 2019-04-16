#!/usr/bin/python3
"""
script to takes url and sends request
"""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.info()['X-Request-Id'])
