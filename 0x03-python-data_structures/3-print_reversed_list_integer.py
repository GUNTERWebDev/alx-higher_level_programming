#!/usr/bin/python3
from 3-main import *


def print_reversed_list_integer(my_list=[]):
    rev = list(reversed(my_list))
    for i in rev:
        print("{}".format(i))
