#!/usr/bin/python3

for num in range(0, 99):
    if (chr(num) != 'q' and chr(num) != 'e'):
        print("{} = {}".format(num, hex(num)), end="\n")
