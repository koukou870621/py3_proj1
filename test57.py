#!/usr/bin/python3

import matplotlib.pyplot as plt


def test57():
    y = [0, 1]
    x = [0, 1]
    plt.plot(x, y, label='y=x')
    plt.title('Simple line')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.legend()
    plt.show()


test57()
