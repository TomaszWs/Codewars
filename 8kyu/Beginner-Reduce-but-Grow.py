# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
#
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24


def grow(arr):
    r = arr[0]
    arr.pop(0)
    for i in arr:
        r = r * i
    return r


if __name__ == '__main__':
    print(grow([1, 2, 3, 4]))


# Best solutions:


def grow(arr):
	product = 1
	for i in arr:
		product *= i
	return product


import math


def grow(arr):
    return math.prod(arr)


from functools import reduce


def grow(arr):
    return reduce(lambda x, y: x * y, arr)
