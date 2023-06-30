#!/usr/bin/python3
"""
this is "4-print_square"
functions:
    def print_square(size):
"""
def print_square(size):
    """
    funcion that print square

    Args:
        size (int): size
    """
    i = 0
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        while i < size:
            j = 0
            while j < size:
                print("#", end="")
                j += 1
            print("")
            i += 1
