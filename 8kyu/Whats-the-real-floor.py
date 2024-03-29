# Americans are odd people: in their buildings, the first floor is actually
# the ground floor and there is no 13th floor (due to superstition).
#
# Write a function that given a floor in the american system returns the floor
# in the european system.
#
# With the 1st floor being replaced by the ground floor and the 13th floor
# being removed, the numbers move down to take their place. In case of
# above 13, they move down by two because there are two omitted numbers
# below them.
#
# Basements (negatives) stay the same as the universal level.
#
# More information here
# Examples
#
# 1  =>  0
# 0  =>  0
# 5  =>  4
# 15  =>  13
# -3  =>  -3


def get_real_floor(n):
    if n == 0:
        return 0
    else:
        if 0 < n < 13:
            return n-1
        elif n > 13:
            return n-2
        else: return n


print(get_real_floor(-3))


# Best solutions:


def get_real_floor(n):
    if n <= 0: return n
    if n < 13: return n-1
    if n > 13: return n-2


def get_real_floor(n):
    return n if n < 1 else n - 1 if n < 13 else n - 2


def get_real_floor(n):
    return n - (n > 0) - (n > 13)