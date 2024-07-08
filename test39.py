#!/usr/bin/python3

def test39():
    a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100,0]
    temp1, temp2, number, end, i, j = 0, 0, 0, 0, 0, 0
    print("元の配列は:")
    i = 0
    while i < 10:
        print("%4d" % a[i])
        i += 1
    print("新しい番号を挿入する:")
    number = int(input("number:"))
    end = a[9]
    if number > end:
        a[10] = number
    else:
        i = 0
        while i < 10:
            if a[i] > number:
                temp1 = a[i]
                a[i] = number
                j = i+1
                while j < 11:
                    temp2 = a[j]
                    a[j] = temp1
                    temp1 = temp2
                    j += 1
                break
            i += 1
    i = 0
    while i < 11:
        print("%4d" % a[i])
        i += 1


test39()
