#!/usr/bin/python3
'''Module for lookup method.'''

def lookup(obj):

    """ this function returns the methods, attribute in  an  object
    Args:
        obj (object): the object to list.

    Returns:
        list: the list of attributes.
    """ 

    return  (dir(obj))
