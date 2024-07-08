#!/usr/bin/python3

def test5():
    print("")
    x = y = z = t = 0
    print("数字を三つ入力してください：")
    x = input("x:")
    y = input("y:")
    z = input("z:")
    x = int(x)
    y = int(y)
    z = int(z)
    if x > y:
        t = x
        x = y
        y = t
    if x > z:
        t = z
        z = x
        x = t
    if y > z:
        t = y
        y = z
        z = t
    print("小さいものから大きいものまで並べ替えろと：%d %d %d" % (x, y, z))


test5()
