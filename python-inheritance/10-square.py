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

        Note:
            Size is validated using the integer_validator from BaseGeometry.
            Rectangle parent is initialized with size both width and height.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
