# Your Job
#
# Find the sum of all multiples of n below m
# Keep in Mind
#
#     n and m are natural numbers (positive integers)
#     m is excluded from the multiples
#
# Examples
#
# sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
# sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
# sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
# sumMul(4, -7)  ==> "INVALID"


def sum_mul(n, m):
    return sum(range(n, m, n)) if n > 0 and m > 0 else "INVALID"


if __name__ == '__main__':
    print(sum_mul(2, 9))


# Best solutions:


def sum_mul(n, m):
    if m>0 and n>0:
        return sum(range(n, m, n))
    else:
        return 'INVALID'
