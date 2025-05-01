# This series of katas will introduce you to basics of doing geometry with
# computers.
#
# Point objects have x, y attributes. Circle objects have center which is a
# Point, and radius, which is a number.
#
# Write a function calculating circumference of a Circle.
#
# Tests round answers to 6 decimal places.


from math import pi


def circle_circumference(circle):
    return round(2 * pi * circle.radius, 6)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


if __name__ == '__main__':
    circle = Circle(Point(10, 10), 30)
    print(circle_circumference(circle))


# Best solutions:


from math import pi


def circle_circumference(circle):
    return round(2 * circle.radius * pi, 6)


from math import pi


def circle_circumference(circle):
    return 2 * pi * circle.radius