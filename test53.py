#!/usr/bin/python3

def test53():
    a, b = 0, 0
    a = 0o77
    b = a ^ 3
    print("bの値は%d" % b)
    b ^= 7
    print("bの値は%d" % b)

test53()
