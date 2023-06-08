#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    ln = len(argv) - 1
    if ln == 0:
        print("{} argument.".format(ln))
    else:    
        print("{} argument:".format(ln))
    for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))
