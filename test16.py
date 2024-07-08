#!/usr/bin/python3

def test16():
    a, b, t, r, n = 0, 0, 0, 0, 0
    a = input("a:")
    b = input("b:")
    a = int(a)
    b = int(b)
    if a < b:
        t = b
        b = a
        a = t
    r = a % b
    n = a*b
    while r != 0:
        a = b
        b = r
        r = a % b
    print("これら二つの数値の最大公約数は%dで、最小公倍数は%dです。" % (b, int(n/b)))


test16()
