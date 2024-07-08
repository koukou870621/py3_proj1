#!/usr/bin/python3

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def test25():
    sum = 0
    for i in range(1, 21):
        sum += factorial(i)
    print("1 + 2! + 3! + ... + 20!合計は: %d" % sum)


test25()
