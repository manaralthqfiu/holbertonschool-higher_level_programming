#!/usr/bin/python3
"""
Function that returns the dictionary description of an object
for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of an object's attributes.

    Args:
        obj: Instance of a class.

    Returns:
        dict: A dictionary containing all serializable attributes.
    """
    return obj.__dict__
