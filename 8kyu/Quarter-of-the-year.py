# Given a month as an integer from 1 to 12, return to which quarter of the year
# it belongs as an integer number.
#
# For example: month 2 (February), is part of the first quarter; month 6
# (June), is part of the second quarter; and month 11 (November), is part of
# the fourth quarter.
#
# Constraint:
#
#     1 <= month <= 12


def quarter_of(month):
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    else: return 4


if __name__ == '__main__':
    print(quarter_of(6))


# Best solutions:


def quarter_of(month):
    # your code here
    if month in range(1, 4):
        return 1
    elif month in range(4, 7):
        return 2
    elif month in range(7, 10):
        return 3
    elif month in range(10, 13):
        return 4


from math import ceil


def quarter_of(month):
    return ceil(month / 3)


def quarter_of(n):
    return (n + 2) // 3
