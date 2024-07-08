#!/usr/bin/python3

def test54():
    print("整数を入力してください:")
    a, b, c, d = 0, 0, 0, 0
    a = int(input("a:"),8)
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    print("%o\n%o\n" % (a, d))


test54()
