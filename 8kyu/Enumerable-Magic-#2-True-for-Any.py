# The task is to write a function that accepts two parameters: an array and a
# callback function (in Ruby: a block).
#
# The function should return true if the callback function / block returns true
# for any item in the array, otherwise return false.
#
# The function should return false if the array is empty.


def any_(lst, func):
    return any(map(func, lst))


if __name__ == '__main__':
    print(any_([0, 1, 2, 3, 5, 8, 13], lambda x: x % 2 == 0))


# Best solutions:


def any_(lst, func):
    return any(func(item) for item in lst)


def any_(lst, func):
    if not lst:
        return False
    for item in lst:
        if func(item):
            return True
    return False
