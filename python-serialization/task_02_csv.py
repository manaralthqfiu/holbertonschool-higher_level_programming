#!/usr/bin/python3
"""
Module that converts CSV data into JSON format and saves it to data.json.
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Converts a CSV file into JSON format and writes it to data.json.

    Args:
        filename (str): The CSV file to read.

    Returns:
        bool: True if conversion succeeds, False otherwise.
    """
    try:
        data_list = []

        # Read CSV file
        with open(filename, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_list.append(row)

        # Write JSON output
        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data_list, jsonfile, indent=4)

        return True

    except Exception:
        return False
