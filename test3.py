#!/usr/bin/python3

# elpy-autopep8-fix-code
def test3():
    i = j = m = n = x = 0
    for i in range(1, int(168/2)+1):
        if 168 % i == 0:
            j = 168/i
            if i > j and (i+j) % 2 == 0 and (i-j) % 2 == 0:
                m = (i+j)/2
                n = (i-j)/2
                x = n*n-100
                print("%d+100=%d*%d" % (x, n, n))
                print("%d+268=%d*%d" % (x, m, m))


test3()
