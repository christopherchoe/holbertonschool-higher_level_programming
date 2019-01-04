#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0,0)):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        if isinstance(position, tuple) and len(position) == 2\
            and position[0] >= 0 and position[1] >= 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        for p in range(0, self.__position[1]):
            print('')
        for i in range(0, self.__size):
            for p in range(0, self.__position[0]):
                print(' ', end='')
            for i in range(0, self.__size):
                print("#", end='')
            print('')
        if self.__size == 0:
            print('')

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2\
            and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
