#!/usr/bin/python3

def test24():
    i, t = 0, 0
    sum, a, b = 0.0, 2.0, 1.0
    for i in range(1, 21):
        sum = sum+a/b
        t = a
        a = a+b
        b = t
    print("%9.6f" % sum)


test24()
