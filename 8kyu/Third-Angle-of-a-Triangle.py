# You are given two interior angles (in degrees) of a triangle.
#
# Write a function to return the 3rd.
#
# Note: only positive integers will be tested.
#
# https://en.wikipedia.org/wiki/Triangle


def other_angle(a, b):
    return 180 - a - b


if __name__ == '__main__':
    print(other_angle(30, 60))


# Best solutions:


def other_angle(a, b):
    if (a or b) < 0:
        return "angle cannot be smaller than 0"

    else:
        return 180 - (a + b)
