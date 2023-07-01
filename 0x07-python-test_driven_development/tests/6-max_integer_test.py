#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""
    def ordred(self):
        """test ordred list"""
        ordred = [1, 2, 3, 4]
        self.assertAlmostEqual(max_integer(ordred), 4)
    def unordred(self):
        unordred = [1, 2, 5, 3]
        self.assertAlmostEqual(max_integer(unordred), 5)
    
        """test listwith one element"""
    def unordred(self):
        one = [9]
        self.assertAlmostEqual(max_integer(one), 9)
    
    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)
    def test_floats(self):
        """Test a list of floats."""
        floats = [2.55, 8.33, -9.13, 30.2, 8.0]
        self.assertEqual(max_integer(floats), 30.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
