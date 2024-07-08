#!/usr/bin/python3

def test29():
    a, b, c, d, e, x = 0, 0, 0, 0, 0, 0
    x = input("五桁を入力してください:")
    x = int(x)
    a = x/10000
    b = x % 10000/1000
    c = x % 1000/100
    d = x % 100/10
    e = x % 10
    if a != 0:
        print("は五桁の数字で、その逆の順序は: %d %d %d %d %d" % (e, d, c, b, a))
    elif b != 0:
        print("は四桁の数字で、その逆の順序は: %d %d %d %d" % (e, d, c, b))
    elif c != 0:
        print("は三桁の数字で、その逆の順序は: %d %d %d" % (e, d, c))
    elif d != 0:
        print("は二桁の数字で、その逆の順序は: %d %d" % (e, d))
    elif e != 0:
        print("は一桁の数字で、その逆の順序は: %d" % e)


test29()
