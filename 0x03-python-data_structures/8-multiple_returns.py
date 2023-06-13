#!/usr/bin/python3

def multiple_returns(sentence):
    len = len(sentence)
    if len == 0:
        return (0, None)
    else:
        c = sentence[0]
        return (len, c)
