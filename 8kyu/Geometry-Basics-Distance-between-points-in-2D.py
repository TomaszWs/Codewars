# This series of katas will introduce you to basics of doing geometry with
# computers.
#
# Point objects have attributes x and y.
#
# Write a function calculating distance between Point a and Point b.
#
# Input coordinates fit in range −50⩽x,y⩽50 -50 \leqslant x,y \leqslant
# 50 −50⩽x,y⩽50. Tests compare expected result and actual answer with
# tolerance of 1e-6.


def distance_between_points(a, b):
    return (((a.x - b.x) ** 2) + ((a.y - b.y) ** 2)) ** 0.5


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    print(distance_between_points(Point(3, 3), Point(3, 3)))


# Best solutions:


from math import hypot


def distance_between_points(a, b):
    return hypot(a.x - b.x, a.y - b.y)


import math


def distance_between_points(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


from math import dist


def distance_between_points(a, b):
    # your code here
    return dist((a.x, a.y),(b.x, b.y))
