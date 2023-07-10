#!/usr/bin/python3
"""
This is '7-base_geometry' module.
Functions and Classes:
    class BaseGeometry
"""


class BaseGeometry:
    """
    BaseGeometry
    """
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")
        """raises an valueerror and type error"""
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))
