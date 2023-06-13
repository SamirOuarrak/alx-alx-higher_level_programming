#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) == 1:
            nb1 = (tuple_a[0], 0)
        else:
            nb1 = (0, 0)
    else:
        nb1 = (tuple_a[0], tuple_a[1])
    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            nb2 = (tuple_b[0], 0)
        else:
            nb2 = (0, 0)
    else:
        nb2 = (tuple_b[0], tuple_b[1])
    new_tuple = (nb1[0] + nb2[0], nb1[1] + nb2[1])
    return (new_tuple)
