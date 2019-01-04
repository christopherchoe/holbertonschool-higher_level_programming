#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError
        else:
            raise TypeError
