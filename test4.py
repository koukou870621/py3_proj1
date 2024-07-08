#!/usr/bin/python3


def case1():
    return 0


def case2():
    return 31


def case3():
    return 59


def case4():
    return 90


def case5():
    return 120


def case6():
    return 151


def case7():
    return 181


def case8():
    return 212


def case9():
    return 243


def case10():
    return 273


def case11():
    return 304


def case12():
    return 334


switch = {
    1: case1,
    2: case2,
    3: case3,
    4: case4,
    5: case5,
    6: case6,
    7: case7,
    8: case8,
    9: case9,
    10: case10,
    11: case11,
    12: case12
}


def test4():
    day = month = year = sum = leap = 0
    print("年、月、日を次の形式で入力してください：年、月、日")
    year = input("input year:")
    month = input("input month:")
    day = input("input day:")
    year = int(year)
    month = int(month)
    day = int(day)
    sum = switch.get(month, lambda: print("data error"))()
    sum = sum+day
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        leap = 1
    else:
        leap = 0
    if leap == 1 and month > 2:
        sum += 1
    print("これは年の%d日です。" % sum)


test4()
