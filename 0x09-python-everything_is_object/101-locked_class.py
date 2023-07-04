#!/usr/bin/python3
"""
this is "101-locked_class"
classes:
    LockedClass

"""


class LockedClass:
    """
     that prevents the user from dynamically creating new instance attributes,
     except if the new instance attribute is called first_name.
    """
    __slots__ = ['first_name']
