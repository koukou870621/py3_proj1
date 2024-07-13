#!/usr/bin/python3

import matplotlib.pyplot as plt


def test63():
    center_x = 0
    center_y = 0
    width = 4
    height = 2
    angle = 30
    ellipse = plt.matplotlib.patches.Ellipse(
        (center_x, center_y), width, height, angle=angle, edgecolor='r', facecolor='none'
    )
    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
    ax.add_patch(ellipse)
    ax.set_xlim(center_x-width, center_x+width)
    ax.set_ylim(center_y-height, center_y+height)
    plt.grid(True)
    plt.title('Ellipse')
    plt.show()


test63()
