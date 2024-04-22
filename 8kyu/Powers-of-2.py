# Complete the function that takes a non-negative integer n as input, and
# returns a list of all the powers of 2 with the exponent ranging
# from 0 to n ( inclusive ).

# Examples
#
# n = 0  ==> [1]        # [2^0]
# n = 1  ==> [1, 2]     # [2^0, 2^1]
# n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]


def powers_of_two(n):
    return [2**p for p in range(0,n+1)]


print(powers_of_two(2))


# Best solutions:


def powers_of_two(n):
    return [2**x for x in range(n+1)]


def powers_of_two(n):
    a = []
    for i in range(0, n + 1):
        a.append(2 ** i)
    return a


def powers_of_two(n):
    return [1<<x for x in range(n + 1)]
