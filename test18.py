#!/usr/bin/python3

def test18():
    s, a, n, t = 0, 0, 0, 0
    a = input("a:")
    n = input("n:")
    a = int(a)
    n = int(n)
    t = a
    while n > 0:
        s += t
        a = a*10
        t += a
        n -= 1
    print("a+aa+...=%d" % s)


test18()
