#!/usr/bin/python3
"""
This is '0-add_integer' module.
Functions:
    add_ineger(a, b=98)
"""
def add_integer(a, b=98):
    """
    calculate the sum

    Args:
        a (int): num
        b (int, optional): num. Defaults to 98.

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        int: sum between args
    """
    if type(a) != int:
        if type(a) is float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) != int:
        if type(b) is float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b

