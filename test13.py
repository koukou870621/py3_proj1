#!/usr/bin/python3

def test13():
    i, x, y, z = 0, 0, 0, 0
    for i in range(100, 1000):
        x = i % 10
        y = int(i/10) % 10
        z = int(i/100) % 10
        if i == (x*x*x+y*y*y+z*z*z):
            print("%d" % i)


test13()
