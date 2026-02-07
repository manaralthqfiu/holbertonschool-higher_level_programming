#!/usr/bin/python3
"""
Custom class with pickle-based serialization and deserialization.
"""

import pickle


class CustomObject:
    """
    A simple class representing a custom object with basic attributes.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the object's attributes in a formatted way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current object instance to a file using pickle.

        Args:
            filename (str): The file to save the serialized object.

        Returns:
            None if an error occurs.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a pickle file.

        Args:
            filename (str): The file to load the object from.

        Returns:
            CustomObject instance or None if an error occurs.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
