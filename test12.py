#!/usr/bin/python3

def test12():
    i, j, count = 0, 0, 0
    for i in range(101, 201):
        for j in range(2, i+1):
            if i % j == 0:
                break
        if j >= i:
            count += 1
            print("%d " % i, end='')
            if count % 5 == 0:
                print("")


test12()
