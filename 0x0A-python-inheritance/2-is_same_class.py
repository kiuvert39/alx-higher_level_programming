#!/usr/bin/python3
'''function for instance  of a class.'''


def is_same_class(obj, a_class):
    """check if an  object is  an  instance of a class.
    Args:
            obj (object): the object to list.
            a_class (class): instance of class.
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
