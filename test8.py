#!/usr/bin/python3

def test8():
    print("")
    i, j, result = 0, 0, 0
    for i in range(1, 10):
        for j in range(1, i+1):
            result = i*j
            print("%d*%d=%-3d" % (i, j, result),end='')
        print("")


test8()
