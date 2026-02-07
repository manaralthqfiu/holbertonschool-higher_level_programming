#!/usr/bin/python3
"""
Basic serialization and deserialization using JSON.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to JSON and saves it to a file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The output JSON filename.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads JSON data from a file and deserializes it into a Python dictionary.

    Args:
        filename (str): The JSON file to read.

    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
