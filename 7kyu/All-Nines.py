# Task
#
# Given any positive integer x ≤ 4000, find the smallest positive integer m
# such that mx consists of all 9's. Return -1 if no such m exists.
# Examples:
#
# 11 -> 9, because 11 * 9 == 99.
#
# 12 -> -1, because 12 is even, so no multiple of it can contain only nines.
#
# 13 -> 76923, because 13 * 76923 == 999999, and no smaller positive integer,
# when multiplied by 13, generates an integer containing only nines.
#
# NOTE: Although x ≤ 4000, m can be very very LARGE. Where necessary, the way
# of handling big integers appropriate to the language should be used.


def all_nines(x):
    if any(x % i == 0 for i in [2, 4, 5, 6, 8, 10]):
        return -1

    current_nines = 9
    while current_nines % x != 0:
        current_nines = current_nines * 10 + 9
    return current_nines // x


if __name__ == "__main__":
    print(all_nines(13))


# Best solutions:


def all_nines(k):
    if k % 2 == 0 or k % 5 == 0:
        return -1
    n = 9
    while n % k != 0:
        n = n * 10 + 9
    return n // k


def all_nines(x):
    if x % 2 == 1:
        for n in range(1, 4000):
            nines = 10 ** n - 1
            if nines % x == 0:
                return nines // x

    return -1


def all_nines(x):
    if 0 in {x % 2, x % 5}:
        return -1
    n = 9
    while n % x:
        n = 10 * n + 9
    return n // x
