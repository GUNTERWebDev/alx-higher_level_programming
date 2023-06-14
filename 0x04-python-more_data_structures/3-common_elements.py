#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = []
    for j in set_2:
        if j in set_1:
            new_set.append(j)
    return (new_set)
