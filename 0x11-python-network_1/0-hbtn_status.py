#!/usr/bin/python3
"""
script to fetch url
"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    read = response.read()
    print('Body response:')
    print('     - type: {}'.format(type(read)))
    print('     - content: {}'.format(read))
    print('     - utf8 content: {}'.format(read.decode('utf-8')))
