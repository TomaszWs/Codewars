# Task
#
# Given a point in a Euclidean plane (x and y), return the quadrant the point
# exists in: 1, 2, 3 or 4 (integer). x and y are non-zero integers, therefore
# the given point never lies on the axes.
# Examples
#
# (1, 2)     => 1
# (3, 5)     => 1
# (-10, 100) => 2
# (-1, -9)   => 3
# (19, -56)  => 4
#
# Reference
# [Quadrants] Quadrants
#
# There are four quadrants:
#
#     First quadrant, the quadrant in the top-right, contains all points with
#     positive X and Y
#     Second quadrant, the quadrant in the top-left, contains all points with
#     negative X, but positive Y
#     Third quadrant, the quadrant in the bottom-left, contains all points with
#     negative X and Y
#     Fourth quadrant, the quadrant in the bottom-right, contains all points
#     with positive X, but negative Y
#
# More on quadrants: Quadrant (plane geometry) - Wikipedia
# Task Series
#
#     Quadrants (this kata)
#     Quadrants 2: Segments


def quadrant(x, y):
    if x > 0 < y:
        return 1
    elif x < 0 < y:
        return 2
    elif x < 0 > y:
        return 3
    else:
        return 4


if __name__ == '__main__':
    print(quadrant(1, 2))


# Best solutions:


quadrant = lambda x, y: ((1,2),(4,3))[y<0][x<0]


def quadrant(x, y):
    if x >= 0:
        if y >= 0:
            return 1
        else: return 4
    elif x<0:
        if y < 0:
            return 3
        else: return 2


def quadrant(x, y):
    if x == 0 or y == 0:
        return 'x and y must be non-zero integers.'
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4


def quadrant(x, y):
    return 1 + 2*(y<0) + (x*y<0)
