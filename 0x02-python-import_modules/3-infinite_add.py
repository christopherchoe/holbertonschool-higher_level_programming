#!/usr/bin/python3
from sys import argv
added = 0
for i in argv[1:]:
    added += int(i)
print(added)
