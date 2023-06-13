#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    else:
        Max = my_list[0]
        for nb in my_list:
            if nb > Max:
                Max = nb
        return (Max)
