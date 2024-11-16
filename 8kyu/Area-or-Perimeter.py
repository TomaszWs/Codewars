# You are given the length and width of a 4-sided polygon. The polygon can
# either be a rectangle or a square.
# If it is a square, return its area. If it is a rectangle, return its
# perimeter.
#
# Example(Input1, Input2 --> Output):
#
# 6, 10 --> 32
# 3, 3 --> 9
#
# Note: for the purposes of this kata you will assume that it is a square if
# its length and width are equal, otherwise it is a rectangle.


def area_or_perimeter(l , w):
    return l * w if l == w else l * 2 + w * 2


if __name__ == '__main__':
    print(area_or_perimeter(4, 4))


# Best solutions:


def area_or_perimeter(l, w):
    return l * w if l == w else (l + w) * 2


def area_or_perimeter(l, w):
    if l == w:
        tot = l * w
    else:
        tot = l * 2 + w * 2
    return tot

