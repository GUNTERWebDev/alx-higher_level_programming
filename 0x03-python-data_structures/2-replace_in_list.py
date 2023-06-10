#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    count = 0
    for i in my_list:
        if count == idx:
            if my_list[idx] < 0:
                return (my_list)
            else:
                my_list[idx] = element
        count += 1
    if count < idx:
        return (my_list)
