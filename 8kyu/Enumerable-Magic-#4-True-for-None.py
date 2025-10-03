# Write a function that takes two arguments: an array and a callback function
# (in Ruby: a block).
#
# The function should return true if the callback / block returns false for all
# of the items in the array, or if the array is empty; otherwise return false.


def none(lst, func):
    return all(not func(x) for x in lst)


if __name__ == '__main__':
    print(none([0, 1, 2, 3, 5, 8, 13], lambda x: x > 100))


# Best solutions:


def none(lst, func):
    return not any(map(func, lst))
