#!/usr/bin/python3
'''Module for MyList class.'''


class MyList(list):
    """this class   inherite  from  the list    class"""
    def print_sorted(self):
        """this method  prints  a sorted list"""
        print(sorted(self))
