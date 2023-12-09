# Complete the function that takes two integers (a, b, where a < b) and return
# 'an array of all integers between the input parameters, including them.
#
# For example:
#
# a = 1
# b = 4
# --> [1, 2, 3, 4]
#


def between(a,b):
    return [number for number in range(a,b+1)]


a = 1
b = 4
print(between(a,b))

# Best solutions:


def between(a,b):
    return list(range(a,b+1))


def between(a,b):
    arr = []
    for i in range(a, b + 1):
        arr.append(i)
    return arr

