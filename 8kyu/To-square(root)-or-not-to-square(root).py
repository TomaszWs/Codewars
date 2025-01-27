# Write a method, that will get an integer array as parameter and will process
# every number from this array.
#
# Return a new array with processing every number of the input-array like this:
#
# If the number has an integer square root, take this, otherwise square the
# number.
# Example
#
# [4,3,9,7,2,1] -> [2,9,3,49,4,1]
#
# Notes
#
# The input array will always contain only positive numbers, and will never be
# empty or null.


from math import sqrt


def square_or_square_root(arr):
    return [int(sqrt(i)) if sqrt(i).is_integer() else int(pow(i, 2))
            for i in arr]


if __name__ == '__main__':
    print(square_or_square_root([4,3,9,7,2,1]))


# Best solutions:


def square_or_square_root(arr):
    result = []
    for x in arr:
        root = x**0.5
        if root.is_integer():
            result.append(root)
        else:
            result.append(x*x)
    return result


from math import sqrt


def square_or_square_root(arr):
    return [int(sqrt(a)) if sqrt(a) % 1 == 0 else a ** 2 for a in arr]


def square_or_square_root(arr):
    return [i**0.5 if (i**0.5).is_integer() else i**2 for i in arr]
