#!/usr/bin/python3
"""
Defines a Student class with JSON serialization and filtering.
"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes listed in attrs
        will be included in the returned dictionary.

        Args:
            attrs (list): Optional list of attribute names to retrieve.

        Returns:
            dict: A dictionary containing the selected attributes.
        """
        if isinstance(attrs, list):
            # Return only attributes that exist in the instance
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        # Otherwise return all attributes
        return self.__dict__
