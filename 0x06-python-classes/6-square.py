#!/usr/bin/python3
"""module containing square class"""


class Square:
    """representing a square"""
    def __init__(self, size=0, position=(0, 0)) -> None:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, val):
        if type(val) != tuple or len(val) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif val[0] < 0 or val[1] < 0 or val[0] != int or val[1] != int:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = val

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print("\n", end='')
