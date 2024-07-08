#!/usr/bin/python3

def test26():
    i = 0
    for i in range(6):
        print("%d!=%d" % (i, fact(i)))


def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j*fact(j-1)
    return sum


test26()
