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
    if obj.__class__ == a_class:
        return False
    if obj.__class__.__name__ == 'object':
        return False
    return inherits_from(obj.__class__.__base__, a_class)
