#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.

    >>> add_integer(1, 2)
    3
    >>> add_integer(2.5, 2)
    4
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
