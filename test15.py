#!/usr/bin/python3

def test15():
    score = grade = 0
    score = input("スコアを入力してください：")
    score = int(score)
    grade = 'A' if score >= 90 else ('B' if score >= 60 else 'C')
    print("%c" % grade)


test15()
