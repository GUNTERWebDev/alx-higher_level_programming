#!/usr/bin/python3
def search_replace(my_list, search, replace):
    count = 0
    for i in my_list:
        if i == search:
            my_list[count] = replace
        count += 1
    return (my_list)
