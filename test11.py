#!/usr/bin/python3

def test11():
    f1, f2, i = 1, 1, 0
    for i in range(1, 21):
        print("%12d%12d" % (f1, f2), end='')
        if i % 2 == 0:
            print("")
        f1 = f1+f2
        f2 = f1+f2


test11()
