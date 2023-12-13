# Your task is to construct a building which will be a pile of n cubes. The
# cube at the bottom will have a volume of n3 n^3 n3, the cube above will have
# volume of (n−1)3 (n-1)^3 (n−1)3 and so on until the top which will have a
# volume of 13 1^3 13.
#
# You are given the total volume m of the building. Being given m can you find
# the number n of cubes you will have to build?
#
# The parameter of the function findNb (find_nb, find-nb, findNb, ...) will be
# an integer m and you have to return the integer n such as
# n3+(n−1)3+(n−2)3+...+13=m n^3 + (n-1)^3 + (n-2)^3 + ... + 1^3 = m n3+(n−1)3+(n−2)3+...+13=m if such a n exists or -1 if there is no such n.
# Examples:
#
# findNb(1071225) --> 45
#
# findNb(91716553919377) --> -1


def find_nb(m):
    n = 1
    while (n * (n + 1) // 2) ** 2 < m:
        n += 1
    return n if (n * (n + 1) // 2) ** 2 == m else -1


m = 1071225
print(find_nb(m))

# Best solutions:


def find_nb(m):
    n = 1
    volume = 0
    while volume < m:
        volume += n**3
        if volume == m:
            return n
        n += 1
    return -1


from math import floor, sqrt

def find_nb(m):
    # Used the formula for the sum of cubes: m = (n(n+1)/2)^2
    # Rearranged to find n^2 + n = n(n+1) ~= n^2 ~= 2sqrt(m),
    # so take square root and round down the result.
    n_canidate = int(floor(sqrt(2 * sqrt(m))))
    if (n_canidate * (n_canidate + 1) / 2 )**2 == m:
        return n_canidate
    else:
        return -1
