#!/usr/bin/python3

def test20():
    print("")
    h, s = 100.0, 100.0
    h = h/2
    for i in range(2, 11):
        s = s+2*h
        h = h/2
    print("１０回目の着地時には合計%fメートルを通過し、１０回目のリバウンドの高さは%fメートルでした。" % (s, h))


test20()
