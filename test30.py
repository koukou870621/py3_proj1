#!/usr/bin/python3

def test30():
    ge, shi, qian, wan, x = 0, 0, 0, 0, 0
    x = input("五文字を入力してください:")
    x = int(x)
    wan = int(x/10000)
    qian = int(x % 10000/1000)
    shi = int(x % 100/10)
    ge = x % 10
    if ge == wan and shi == qian:
        print("これは回文数字です")
    else:
        print("これは回文ではありません")


test30()
