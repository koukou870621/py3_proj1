#!/usr/bin/python3

def test19():
    i, j, k, n, sum = 0, 0, 0, 0, 0
    N = 1000
    a = [0] * 256
    for i in range(2, N+1):
        sum = a[0] = 1
        k = 0
        for j in range(2, int(i/2)+1):
            if i % j == 0:
                sum += j
                k += 1
                a[k] = j
        if i == sum:
            print("%d=%d" % (i, a[0]),end='')
            for n in range(1, k+1):
                print("+%d" % a[n], end='')
            print("")


test19()
