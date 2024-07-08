#!/usr/bin/python3

def test51():
    a, b = 0, 0
    a = 0o77
    b = a & 3
    print("a & b(decimal)は%d" % b)
    b &= 7
    print("a & b(decimal)は%d" % b)


test51()
