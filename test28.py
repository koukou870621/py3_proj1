#!/usr/bin/python3

def age(n):
    c = 0
    if n == 1:
        c = 10
    else:
        c = age(n-1)+2
    return c


def test28():
    print("%d" % age(5))


test28()
