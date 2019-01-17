#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """
    reads n lines of text file and prints to stdout
    """
    count = 1
    with open(filename) as f:
        for line in f:
            print(line, end='')
            if nb_lines > 0:
                count += 1
            if count > nb_lines and nb_lines > 0:
                break
