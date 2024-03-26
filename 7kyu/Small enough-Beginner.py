# You will be given an array and a limit value. You must check that all values
# in the array are below or equal to the limit value. If they are, return true.
# Else, return false.
#
# You can assume all values in the array are numbers.


def small_enough(array, limit):
    return all(value <= limit for value in array)


print(small_enough([66, 101],200))


# Best solutions:


def small_enough(array, limit):
    return max(array)<=limit


def small_enough(array, limit):
    for e in array:
        if not e <= limit: return False
    return True


def small_enough(array, limit):
    for number in array:
        if number > limit: return False
    return True