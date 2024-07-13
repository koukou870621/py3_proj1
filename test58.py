#!/usr/bin/python3

import matplotlib.pyplot as plt
import matplotlib.patches as pat


def test58():
    fig, ax = plt.subplots()
    rectangle = pat.Rectangle((0.1, 0.1), 0.5, 0.3,
                              edgecolor='blue', facecolor='none')
    ax.add_patch(rectangle)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.title('Simple Rectangle')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.show()


test58()
