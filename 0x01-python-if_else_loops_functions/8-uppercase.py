#!/usr/bin/python3
def uppercase(str):
    for char in str:
        char = ord(char)
        if char in range(97, 123):
            char -= 32
            print("{:c}".format(char), end='')
        else:
            print("{:c}".format(char), end='')
    print('\n')
