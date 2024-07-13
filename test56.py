#!/usr/bin/python3

import matplotlib.pyplot as plt
import matplotlib.patches as patches


def test56():
    print("")
    fig, ax = plt.subplots()
    circle = patches.Circle(
        (0.5, 0.5), 0.3, edgecolor='blue', facecolor='none')
    ax.add_patch(circle)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    plt.show()


test56()
