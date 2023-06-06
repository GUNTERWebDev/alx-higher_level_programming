#!/usr/bin/python3
count = 1
for i in reversed(range(97, 123)):
    if count % 2 == 0:
        i -= 32
    print("{:c}".format(i), end='')
    count += 1
