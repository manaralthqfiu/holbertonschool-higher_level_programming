#!/usr/bin/python3
"""
Module that contains the read_file function.
Reads a UTF-8 text file and prints its content to stdout.
"""

def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
