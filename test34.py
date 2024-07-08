#!/usr/bin/python3

def hello_world():
    print("Hello, world!")


def three_hellos():
    print("")
    counter = 0
    for counter in range(1, 4):
        hello_world()


def test34():
    three_hellos()


test34()
