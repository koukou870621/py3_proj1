#!/usr/bin/python3

def test22():
    i, j, k = 0, 0, 0
    x = ord('x')
    z = ord('z')
    for i in range(x, z+1):
        for j in range(x, z+1):
            if i != j:
                for k in range(x, z+1):
                    if i != k and j != k:
                        if i != x and k != x and k != z:
                            print("注文は: a--%c  b--%c  c--%c" %
                                  (i, j, k))


test22()
