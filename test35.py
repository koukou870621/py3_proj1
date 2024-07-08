#!/usr/bin/python3

def reverse(s):
    lens = len(s)
    p = list(s)
    i = 0
    c = 0
    while i <= lens/2-1:
        c = p[i]
        p[i] = p[lens-1-i]
        p[lens-1-i] = c
        i += 1
    return ''.join(p)


def test35():
    s = "www.runoob.com"
    print("'%s'=>" % s, end='')
    r = reverse(s)
    print("'%s'" % r)


test35()
