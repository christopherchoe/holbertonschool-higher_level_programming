#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    appends a string to end of text file, retuns number of characters
    """
    with open(filename, "a") as f:
        return f.write(str(text))
