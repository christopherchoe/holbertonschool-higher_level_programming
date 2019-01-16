#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    return True if object is instance of class or inherited from
    return Falase otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
