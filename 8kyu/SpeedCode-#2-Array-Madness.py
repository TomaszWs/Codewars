# SpeedCode #2 - Array Madness
# Objective
#
# Given two integer arrays a, b, both of length >= 1, create a program that
# returns true if the sum of the squares of each element in a is strictly
# greater than the sum of the cubes of each element in b.
#
# E.g.
#
# array_madness([4, 5, 6], [1, 2, 3]) => True #because 4 ** 2 + 5 ** 2 + 6 **
# 2 > 1 ** 3 + 2 ** 3 + 3 ** 3
#
# Get your timer out. Are you ready? Ready, get set, GO!!!


def array_madness(a,b):
    # Ready, get, set, GO!!!
    return sum(i ** 2 for i in a) > sum(j ** 3 for j in b)


if __name__ == '__main__':
    print(array_madness([4, 5, 6], [1, 2, 3]))
    print(array_madness([1, 2, 3],[4, 5, 6]))


# Best solutions:


def array_madness(a,b):
    return sum(map(lambda a: a ** 2, a)) > sum(map(lambda b: b ** 3, b))


def array_madness(a,b):
    return True if sum([x**2 for x in a]) > sum([y**3 for y in b]) else False


def array_madness(a,b):
    sa=0
    sb=0
    for i in range(0,len(a)):
        sa+=a[i]**2
    for i in range(0,len(b)):
        sb+=b[i]**3
    return sa>sb
