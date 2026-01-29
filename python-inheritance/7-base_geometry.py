#!/usr/bin/python3
"""
This module defines a class BaseGeometry with area and integer_validator.
"""


class BaseGeometry:
    """
    A class representing base geometry.
    """

    def area(self):
        """
        Public instance method that raises an Exception.
        This method is intended to be overridden by subclasses.

        Raises:
            Exception: with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is an integer greater than 0.

        Args:
            name (str): The name associated with the value.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
