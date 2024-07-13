#!/usr/bin/python3

import matplotlib.pyplot as plt


def test62():
    fig, ax = plt.subplots()
    ax.scatter(0.5, 0.5, color='red', s=100)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.title('single point')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.show()


test62()
