#!/usr/bin/python3
"""
XML serialization and deserialization using ElementTree.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML and saves it to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The XML output filename.
    """
    try:
        root = ET.Element("data")

        # Add dictionary items as XML elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

    except Exception:
        return False

    return True


def deserialize_from_xml(filename):
    """
    Deserializes XML data from a file into a Python dictionary.

    Args:
        filename (str): The XML file to read.

    Returns:
        dict: The reconstructed dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result

    except Exception:
        return None
