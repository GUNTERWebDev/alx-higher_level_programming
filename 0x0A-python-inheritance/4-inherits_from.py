#!/usr/bin/python3
"""
This is '4-inherits_from' module.
Functions and Classes:
    def inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """
    check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    """
    same = issubclass(obj.__class__, a_class)
    diff = (obj.__class__ is not a_class)

    return (same and diff)
