#!/usr/bin/python3
"""module containing square class"""


class Square:
    """representing a square"""
    def __init__(self, size=0) -> None:
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
