#!/usr/bin/python3
"""
script to fetch url
"""
import requests


read = requests.get('https://intranet.hbtn.io/status')
print('Body response:')
print('\t- type: {}'.format(type(read.text)))
print('\t- content: {}'.format(read.text))
