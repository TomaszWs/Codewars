# Return the Nth Even Number
#
# Example(Input --> Output)
#
# 1 --> 0 (the first even number is 0)
# 3 --> 4 (the 3rd even number is 4 (0, 2, 4))
# 100 --> 198
# 1298734 --> 2597466
#
# The input will not be 0.


def nth_even(n):
    return (n - 1) * 2


if __name__ == '__main__':
    print(nth_even(3))


# Best solutions:


def nth_even(n):
    return n * 2 - 2
