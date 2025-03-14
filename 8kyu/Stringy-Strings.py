# write me a function stringy that takes a size and returns a string of
# alternating 1s and 0s.
#
# the string should start with a 1.
#
# a string with size 6 should return :'101010'.
#
# with size 4 should return : '1010'.
#
# with size 12 should return : '101010101010'.
#
# The size will always be positive and will only use whole numbers.


def stringy(size):
    return "".join("1" if i % 2 == 0 else "0" for i in range(size))


if __name__ == '__main__':
    print(stringy(3))


# Best solutions:


def stringy(size):
    return ('10' * size)[:size]


def stringy(size):
    return "".join([str(i % 2) for i in range(1, size + 1)])


def stringy(size):
    return '10' * (size // 2) + '1' * (size % 2)
