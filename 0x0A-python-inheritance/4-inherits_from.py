#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
    obj: The object to check.
    a_class: The class to check against.

    Returns:
    True if the object is an instance of a subclass
    of the specified class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
