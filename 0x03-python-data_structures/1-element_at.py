#!/usr/bin/python3
from 1-main import *


def element_at(my_list, idx):
    count = 0
    for i in my_list:
        if count == idx:
            if my_list[idx] < 0:
                return (None)
            else:
                return (my_list[count])
        count += 1
    if count > idx:
        return (None)
