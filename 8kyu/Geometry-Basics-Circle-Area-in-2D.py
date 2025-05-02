# This series of katas will introduce you to basics of doing geometry with
# computers.
#
# Write the function circleArea/CircleArea which takes in a Circle object and
# calculates the area of that circle.
# The Circle class can be seen below:
#
# class Circle:
#     def __init__(self, center, radius):
#         self.center = center
#         self.radius = radius
#
# And the Point class can be seen below:
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


from math import pi


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def circle_area(circle):
    return pi * (circle.radius ** 2)


if __name__ == '__main__':
    print(circle_area(Circle(Point(10, 10), 30)))


# Best solutions:


import math


def circle_area(circle):
    return math.pi * circle.radius**2


from math import pi


def circle_area(circle):
    return pi*pow(circle.radius, 2)
