#!/usr/bin/python3

N = 10


def test40():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    i, t = 0, 0
    print("元の配列は:")
    i = 0
    while i < N:
        a[i] = int(input("a[%d]:" % i))
        i += 1
    i = 0
    while i < N/2:
        t = a[i]
        a[i] = a[N-1-i]
        a[N-1-i] = t
        i += 1
    print("ソートされた配列:")
    i = 0
    while i < N:
        print("%d " % a[i])
        i += 1


test40()
