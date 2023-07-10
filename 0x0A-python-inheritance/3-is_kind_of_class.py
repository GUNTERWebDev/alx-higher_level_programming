#!/usr/bin/python3
"""
This is '3-is_kind_of_class' module.
Functions and Classes:
    def is_same_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """
    object is an instance of class or that inherited from, the specified class
    """
    return isinstance(obj, a_class)
