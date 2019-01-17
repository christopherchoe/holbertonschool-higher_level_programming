#!/usr/bin/python3
def read_file(filename=""):
    """
    reads a text file and prints
    """
    with open(filename) as f:
        print(f.read())
