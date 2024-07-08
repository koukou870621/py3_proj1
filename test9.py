#!/usr/bin/python3

def test9():
    i, j = 0, 0
    for i in range(0, 8):
        for j in range(0, 8):
            if (i+j) % 2 == 0:
                print("%c%c" % (219, 219), end='')
            else:
                print("  ", end='')
        print("")


test9()
