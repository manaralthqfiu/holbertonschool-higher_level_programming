#!/usr/bin/python3
"""
Function that creates an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Reads a JSON file and returns the corresponding Python object.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object created from the JSON content.

    Notes:
        - Uses the 'with' statement as required.
        - Does NOT handle exceptions for invalid JSON (as per instructions).
        - Does NOT handle file permission errors.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
