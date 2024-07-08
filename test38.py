#!/usr/bin/python3

import numpy as np

N = 3


def test38():
    i, j, sum = 0, 0, 0
    a = np.zeros((N, N))
    print("マトリックスを入力してください(3*3)：")
    i = 0
    while i < N:
        j = 0
        while j < N:
            print("")
            a[i][j] = input("a[%d][%d]:" % (i, j))
            j += 1
        i += 1
    i = 0
    while i < N:
        sum += a[i][i]
        i += 1
    print("対角線の和は：%d" % sum)


test38()
