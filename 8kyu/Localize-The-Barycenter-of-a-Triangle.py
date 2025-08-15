# The medians of a triangle are the segments that unit the vertices with the
# midpoint of their opposite sides. The three medians of a triangle intersect
# at the same point, called the barycenter or the centroid. Given a triangle,
# defined by the cartesian coordinates of its vertices, we need to localize its
# barycenter or centroid.
#
# Your function receives the coordinates of the three vertices A, B and C as
# three different arguments and outputs the coordinates of the barycenter O,
# rounded to 4 decimals, in an array [xO, yO].
#
# You know that the coordinates of the barycenter are given by the following
# formulas:
# xO=xA+xB+xC3yO=yA+yB+yC3x_O = \frac{x_A + x_B + x_C}{3} \\ y_O = \frac{y_A +
# y_B + y_C}{3}xO​=3xA​+xB​+xC​​yO​=3yA​+yB​+yC​​
#
# The given points form a real or a degenerate triangle but in each case the
# above formulas can be used.
#
# For additional information about this important point of a triangle see at:
# (https://en.wikipedia.org/wiki/Centroid)
#
# Let's see some cases:
#
# ([4, 6], [12, 4], [10, 10]) ------> [8.6667, 6.6667]
#
# ([4, 2], [12, 2], [6, 10]) ------> [7.3333, 4.6667]
#
# Enjoy it and happy coding!!


def bar_triang(point_a, point_b, point_c):
    x = round((point_a[0] + point_b[0] + point_c[0]) / 3, 4)
    y = round((point_a[1] + point_b[1] + point_c[1]) / 3, 4)
    return [x, y]


if __name__ == '__main__':
    print(bar_triang([4, 6], [12, 4], [10, 10]))


# Best solutions:


def bar_triang(a, b, c):
    return [round(sum(x)/3.0, 4) for x in zip(a, b, c)]


def bar_triang(pointA, pointB, pointC): # points A, B and C will never be aligned
    return [round((pointA[0] + pointB[0] + pointC[0]) / 3.0, 4), round((pointA[1] + pointB[1] + pointC[1]) / 3.0, 4)]


from numpy import mean

def bar_triang(*points):
    return [round(mean(dim), 4) for dim in zip(*points)]
