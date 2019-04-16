#!/usr/bin/python3
"""
script to takes url and sends POST request
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    query_string = urllib.parse.urlencode(email)
    data = query_string.encode("ascii")
    with urllib.request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode('utf-8'))
