#!/usr/bin/python3


def test27():
    i = 5
    print("五文字を入力してください\40:\40")
    palin(i)
    print("")


def palin(n):
    next = 0
    if n <= 1:
        next = getchar()
        print("結果を逆順に出力する\40:\40", end='')
        print("%c" % next, end='')
    else:
        next = getchar()
        palin(n-1)
        print("%c" % next, end='')


def getchar():
    str = input("")
    arr = list(str)
    return arr[0]


test27()
