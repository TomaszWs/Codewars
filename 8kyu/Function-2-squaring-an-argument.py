# Now you have to write a function that takes an argument and returns the
# square of it.


def square(n):
    return n ** 2


if __name__ == '__main__':
    print(square(2))


# Best solutions:


def square(n):
    return n*n


def square(n):
    return pow(n, 2)
