#!/usr/bin/python3

def test14():
    print("")
    n, i = 0, 0
    n = input("整数を入力してください:")
    n = int(n)
    print("%d=" % n, end='')
    for i in range(2, n+1):
        while n % i == 0:
            print("%d" % i, end='')
            n = n/i
            if n != 1:
                print("*", end='')
    print("")


test14()
