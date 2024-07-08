#!/usr/bin/python3

def test23():
    i,j,k=0,0,0
    for i in range(3+1):
        for j in range(3-i):
            print(" ",end='')
        for k in range(2*i+1):
            print("*",end='')
        print("")
    for i in range(3):
        for j in range(i+1):
            print(" ",end='')
        for k in range(5-2*i):
            print("*",end='')
        print("")


test23()
