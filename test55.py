#!/usr/bin/python3

def test55():
    a, b = 0, 0
    a = 234
    b = ~a
    print("aのビット単位の否定は（１０進数）%dです。" % b)
    a = ~a
    a = hex(a & 0xffffffff)
    print(f"aのビット単位の否定は(16進数){a}です。")


test55()
