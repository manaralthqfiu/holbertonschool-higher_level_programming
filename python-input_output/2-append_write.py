#!/usr/bin/python3

"""
Module that contains the append_write function.
"""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file and return number of characters."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
