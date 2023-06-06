#!/usr/bin/python3
def uppercase(str):
    for char in str:
        c = ord(char)
        if c in range(97, 123):
            c = chr(c - 32)
        else:
            c = char
        print("{}".format(c), end='')
    print("")
