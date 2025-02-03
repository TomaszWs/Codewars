# Numbers ending with zeros are boring.
#
# They might be fun in your world, but not here.
#
# Get rid of them. Only the ending ones.
#
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
#
# Zero alone is fine, don't worry about it. Poor guy anyway


def no_boring_zeros(n):
    return int("".join([i for i in str(n).rstrip('0')])) if n != 0 else 0


if __name__ == '__main__':
    print(no_boring_zeros(0))


# Best solutions:


def no_boring_zeros(n):
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0


def no_boring_zeros(n):
    if n == 0:
        return n
    while n % 10 == 0:
        n = n / 10
    return n


def no_boring_zeros(n):
    return int(str(n).strip("0")) if n else n
