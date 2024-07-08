#!/usr/bin/python3

def test10():
    i, j = 0, 0
    print("\1\1")
    for i in range(1, 11):
        for j in range(1, i+1):
            print("%c%c" % (219, 219), end='')
        print("")


test10()
