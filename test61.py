#!/usr/bin/python3

import numpy as np


def test61():
    i, j = 0, 0
    a = np.zeros((10, 10))
    i = 0
    while i < 10:
        a[i][0] = 1
        a[i][i] = 1
        i += 1
    i = 2
    while i < 10:
        j = 1
        while j < i:
            a[i][j] = a[i-1][j-1]+a[i-1][j]
            j += 1
        i += 1
    i = 0
    while i < 10:
        j = 0
        while j <= i:
            print("%5d" % a[i][j], end='')
            j += 1
        print("")
        i += 1


test61()
