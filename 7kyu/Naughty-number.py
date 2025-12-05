# There is a naughty number hidden somewhere in the list. Find the
# index of it, if you are strong enough, of course!
# Input:
#
#     You will receive an array of arrays (a list of lists).
#     Each sub-array can only contain either another array or a single
#     number.
#     There will always be at least one sub-array in the input.
#     There will be only one number hidden in the sub-arrays
#
# Output:
#
# Return the index of the first-level sub-array that contains the
# hidden number.
# Examples:
#
# [ [[[]]] , [[]], [], [], [[2]] ] -> index is 4
#
# [ [1] ] -> index is 0
#
# [ [], [8], [] , [] ] -> index is 1
#
# Please, be sure to check out my other katas:
#
#     Highest Average Depth,
#     The Hackers' Taunt,
#     Sorting Singularly Nested Lists by Depth


def naughty_number(arr):
    f = lambda x: x if isinstance(x, int) else any(f(e) for e in x)
    return next(i for i, a in enumerate(arr) if f(a))


if __name__ == '__main__':
    print(naughty_number([ [[[]]] , [[]], [], [], [[2]] ]))


# Best solutions:


def naughty_number(arr):
    return next(i for i, x in enumerate(arr) if any(str.isdigit(c) for c in str(x)))


def naughty_number(lst):
    for i, sublist in enumerate(lst):
        if isinstance(sublist, list):
            while isinstance(sublist, list) and len(sublist) == 1:
                sublist = sublist[0]

            if isinstance(sublist, int):
                return i
    return -1


print(naughty_number([[[[]]], [[]], [], [], [[2]]]))
print(naughty_number([[1]]))
print(naughty_number([[], [8], [], []]))
print(naughty_number([[[], [[[[42]]]]]]))


def search(arr):
    return False if not len(arr) else search(arr[0]) if isinstance(arr[0],list) else arr[0]
def naughty_number(arr):
    for i,subarr in enumerate(arr):
        item=search(subarr)
        if item:
            return i
    raise ValueError("Bad list.")
