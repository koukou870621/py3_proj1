#!/usr/bin/python3

def f(a):
    a = 4


def test():
    print("")
    a = 9
    print("a=%d" % a)
    f(a)
    print("a=%d" % a)


test()
