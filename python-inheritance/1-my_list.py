#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list.
"""


class MyList(list):
    """
    Subclass of list that provides a method to print elements in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        Assumes all elements in the list are of type int.
        """
        print(sorted(self))
