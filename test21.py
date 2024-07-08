#!/usr/bin/python3

def test21():
    day, x1, x2 = 9, 0, 1
    while day > 0:
        x1 = (x2+1)*2
        x2 = x1
        day -= 1
    print("合計は:%d" % x1)


test21()
