#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle class with width and height
    """
    def __init__(self, width, height):
        """
        instantiation with width and height
        """
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
