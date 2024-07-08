#!/usr/bin/python3

def test17():
    c, letters, spaces, digits, others = 0, 0, 0, 0, 0
    str = input("いくつかの文字を入力してください:")
    char_array = list(str)
    for c in char_array:
        if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
            letters += 1
        elif c >= '0' and c <= '9':
            digits += 1
        elif c == ' ':
            spaces += 1
        else:
            others += 1
    print("文字=%d,数字=%d,スペース=%d,その他=%d" % (letters, digits, spaces, others))


test17()
