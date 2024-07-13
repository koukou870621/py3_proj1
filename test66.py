#!/usr/bin/python3

def swap(s1, s2):
    t = 0
    t = s1
    s1 = s2
    s2 = t


def test66():
    a, b, c = 0, 0, 0
    p1, p2, p3 = 0, 0, 0
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    if a > b:
        print("")
        swap(p1,p2)
    if a > c:
        print("")
        swap(p1,p3)
    if b > c:
        print("")
        swap(p2,p3)
    print("")


test66()
