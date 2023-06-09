#!/usr/bin/python3
from 4-main import *


def new_in_list(my_list, idx, element):
    new_list = [element for element in my_list]
    count = 0
    for i in new_list:
        if count == idx:
            if my_list[idx] < 0:
                return (new_list)
            else:
                new_list[idx] = element
        count += 1
    if count > idx:
        return (new_list)
