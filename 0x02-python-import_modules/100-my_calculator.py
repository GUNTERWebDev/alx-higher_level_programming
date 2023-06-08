#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, div, mul, sub
if __name__ == "__main__":
    args = argv
    ln = len(args) - 1
    if ln != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    num_1 = int(args[1])
    num_3 = int(args[3])
    op = args[2]
    if ln == 3:
        if op != '+' and op != '-' and op != '/' and op != '*':
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        if op == '*':
            print("{} * {} = {}".format(num_1, num_3, mul(num_1, num_3)))
        if op == '-':
            print("{} - {} = {}".format(num_1, num_3, sub(num_1, num_3)))
        if op == '+':
            print("{} + {} = {}".format(num_1, num_3, add(num_1, num_3)))
        if op == '/':
            print("{} / {} = {}".format(num_1, num_3, div(num_1, num_3)))
