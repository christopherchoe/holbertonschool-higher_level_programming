#!/usr/bin/python3
"""
peak finder
"""


def find_peak(list_of_integers):
    """
    finds any peak
    """
    length = len(list_of_integers)
    half = length // 2
    if length > 0:
        if length > 1:
            if length == 2:
                return list_of_integers[0] if\
                    list_of_integers[0] > list_of_integers[1] else\
                    list_of_integers[1]
            if list_of_integers[half] > list_of_integers[half - 1]:
                if list_of_integers[half] > list_of_integers[half + 1]:
                    return list_of_integers[half]
                else:
                    ret = find_peak(list_of_integers[half:])
                    if ret is not None:
                        return ret
            return find_peak(list_of_integers[:half])
        else:
            return list_of_integers[0]
