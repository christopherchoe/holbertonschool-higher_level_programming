#!/usr/bin/python3
"""
peak finder
"""


def find_peak(list_of_integers):
    """
    finds any peak
    """
    length = len(list_of_integers)
    if length > 0:
        return re_peak(list_of_integers, length)


def re_peak(list_of_integers, length):
    """
    finds peak using recursion
    """
    if length > 1:
        if list_of_integers[1] > list_of_integers[0]:
            if (length > 2 and list_of_integers[1] > list_of_integers[2])\
                    or length == 2:
                return list_of_integers[1]
            else:
                return re_peak(list_of_integers[2:], length - 2)
        return list_of_integers[0]
    else:
        return list_of_integers[0]
