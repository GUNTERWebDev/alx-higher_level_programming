#!/usr/bin/python3
from 9-main import *


def max_integer(my_list=[]):
    j = 0
    if len(my_list) != 0:
        while j < len(my_list):
            if my_list[0] < my_list[j]:
                my_list = (my_list[j], my_list[0])
            else:
                j += 1
        return (my_list[0])
    else:
        return (None)
