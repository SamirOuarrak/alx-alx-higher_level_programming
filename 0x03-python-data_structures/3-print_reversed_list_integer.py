#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        idx = len(my_list) - 1
        while my_list and idx >= 0:
            print("{:d}".format(my_list[idx]))
            idx -= 1
            