# Build Tower
#
# Build a pyramid-shaped tower, as an array/list of strings, given a positive
# integer number of floors. A tower block is represented with "*" character.
#
# For example, a tower with 3 floors looks like this:
#
# [
#   "  *  ",
#   " *** ",
#   "*****"
# ]
#
# And a tower with 6 floors looks like this:
#
# [
#   "     *     ",
#   "    ***    ",
#   "   *****   ",
#   "  *******  ",
#   " ********* ",
#   "***********"
# ]


def tower_builder(n_floor):
    result = []
    width = (n_floor * 2) - 1
    for i in range(1, 2 * n_floor, 2):
        chars = i * '*'
        line = chars.center(width)
        result.append(line)
    return result


n_floors = 3
print(tower_builder(n_floors))

# Best solutions:


def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]


def tower_builder(n_floors):
    if n_floors == 0:
        return []

    count = 1
    result = []

    for i in range(1, n_floors + 1):
        stars = '*' * (2 * i - 1)
        space = ' ' * (n_floors - i)
        result.append(space + stars + space)

    return result


def tower_builder(n):
    return [" " * (n - i - 1) + "*" * (2*i + 1) + " " * (n - i - 1) for i in range(n)]