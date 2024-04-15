#!/usr/bin/python3
'''function for instance  of a class.'''


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class.
    Args:
    obj: The object to check.
    cls: The class to check against.

    Returns:
    True if the object is an instance of the specified class
    or its subclass, False otherwise.
    """
    return isinstance(obj, a_class)
