#!/usr/bin/python3

import math

MAX = 1000
prime = [0]*MAX


def isPrimeNaive(n):
    if n <= 1:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1


def isPrime(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    limit = math.sqrt(n)
    for i in range(3, int(limit)+1, 2):
        if n % i == 0:
            return 0
    return 1


def sieve():
    prime[0] = 0
    prime[1] = 0
    for i in range(2, MAX):
        prime[i] = 1
    limit = math.sqrt(MAX)
    for i in range(2, int(limit)+1):
        if not prime[i]:
            for j in range(i*i, MAX+1, i):
                prime[j] = 0


def isPrimeSieve(n):
    if not prime[n]:
        return 1
    else:
        return 0


def test33():
    sieve()
    print("N=%d %d" % (1, isPrime(1)))
    print("N=%d %d" % (2, isPrime(2)))
    print("N=%d %d" % (3, isPrime(3)))
    print("N=%d %d" % (4, isPrime(4)))
    print("N=%d %d" % (7, isPrime(7)))
    print("N=%d %d" % (9, isPrime(9)))
    print("N=%d %d" % (13, isPrime(13)))
    print("N=%d %d" % (17, isPrime(17)))
    print("N=%d %d" % (100, isPrime(100)))
    print("N=%d %d" % (23, isPrime(23)))
    print("N=%d %d" % (1, isPrime(1)))


test33()
