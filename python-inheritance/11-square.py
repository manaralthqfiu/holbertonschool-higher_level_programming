#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's side.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            The area (size * size).
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            A string in the format [Square] <width>/<height>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
