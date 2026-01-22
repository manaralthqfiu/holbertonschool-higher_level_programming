#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to define unittests for the max_integer function"""

    def test_ordered_list(self):
        """Test with an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with max value at the beginning of the list"""
        self.assertEqual(max_integer([10, 5, 2, 1]), 10)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test with a list of only one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test with a list containing negative numbers"""
        self.assertEqual(max_integer([-1, -5, -10, -2]), -1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 5, -10, 2]), 5)

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.5, 2.7, 0.5]), 2.7)

    def test_list_of_strings(self):
        """Test with a list of strings (should work based on ASCII)"""
        self.assertEqual(max_integer(["apple", "zebra", "banana"]), "zebra")

if __name__ == '__main__':
    unittest.main()
