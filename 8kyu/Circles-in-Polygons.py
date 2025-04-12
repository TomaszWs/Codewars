# You are the owner of a box making company.
#
# Your company can produce any equal sided polygon box, but plenty of your
# customers want to transport circular objects in these boxes. Circles are a
# very common shape in the consumer industry. Tin cans, glasses, tyres and
# CD's are a few examples of these.
#
# As a result you decide to add this information on your boxes: The largest
# (diameter) circular object that can fit into a given box.


import math


def circle_diameter(sides, side_length):
    return side_length / math.tan(math.pi / sides)


if __name__ == '__main__':
    print(circle_diameter(4, 5))


# Best solutions:


from math import pi, sin, cos


def circle_diameter(sides, side_length):
    deg = pi / sides
    return side_length * cos(deg) / sin(deg)
