#!/usr/bin/python3

N = 10


def test37():
    print("")
    i, j, temp = 0, 0, 0
    a = [0]*N
    print("十個の数字を入力してください:")
    while i < N:
        a[i] = input("a[%d]" % i)
        a[i] = int(a[i])
        i+=1
    i=0
    while i<N-1:
        min=i
        j=i+1
        while j<N:
            
