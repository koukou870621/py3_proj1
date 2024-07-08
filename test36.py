#!/usr/bin/python3

import math


def test36():
    i, j, k, n = 0, 0, 0, 0
    for i in range(2, 101):
        k = int(math.sqrt(i))
        j = 2
        while j <= k:
            if i % j == 0:
                break
            j += 1
        if j > k:
            print("%d " % i, end='')
            n += 1
            if n % 5 == 0:
                print("")


test36()
