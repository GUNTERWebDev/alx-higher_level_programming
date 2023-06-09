#!/usr/bin/python3
from 6-main import *


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            print("{} ".format(j), end='')
        print()
