#!/usr/bin/python3

def case_m():
    print("monday")


def case_w():
    print("wednesday")


def case_f():
    print("friday")


def case_t():
    print("次の文字を入力してください")
    j = input("j:")
    if j == 'u':
        print("tuesday")
    if j == 'h':
        print("thursday")
    return ""


def case_s():
    print("次の文字を入力してください")
    j = input("j:")
    if j == 'a':
        print("saturday")
    if j == 'u':
        print("sunday")
    return ""


def case_default():
    print("error")
    return ""


def switch(case):
    switcher = {
        'm': case_m,
        'w': case_w,
        'f': case_f,
        't': case_t,
        's': case_s
    }
    func = switcher.get(case, case_default)
    return func()


def getchar():
    str = input("")
    arr = list(str)
    return arr[0]


def test31():
    i = 0
    i = input("最初の文字を入力してください:")
    switch(i)


test31()
