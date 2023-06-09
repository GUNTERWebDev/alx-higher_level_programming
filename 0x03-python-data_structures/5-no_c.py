#!/usr/bin/python3
from 5-main import *


def no_c(my_string):
    first_string = my_string.replace("c", "")
    new_string = first_string.replace("C", "")
    return (new_string)
