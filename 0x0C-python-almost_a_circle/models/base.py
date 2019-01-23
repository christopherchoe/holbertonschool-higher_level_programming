#!/usr/bin/python3
"""
base module
"""


class Base:
    """
    Class that makes the base for other classes.
    Manages __nb_objects and public instance attribute id.
    """
    __nb_object = 0

    def __init__(self, id=None):
        """
        initialize with given id or if None increment __nb_objects
        and assign new value to id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object
