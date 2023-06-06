#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if ord(c) <= ord('z') and ord(c) >= ord('a'):
            c = chr(ord(c) - 32)
        print("{}".format(c), end='')
    print("")
