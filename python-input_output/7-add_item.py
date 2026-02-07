#!/usr/bin/python3
"""
Script that loads a list from add_item.json, adds command-line arguments,
and saves the updated list back to the file.
"""

import sys
from os.path import exists
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

# Load existing list if file exists, otherwise start with empty list
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add all command-line arguments (excluding script name)
items.extend(sys.argv[1:])

# Save updated list
save_to_json_file(items, filename)
