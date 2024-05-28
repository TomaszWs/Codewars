# This code does not execute properly. Try to figure out why.


def multiply(a, b):
    return a * b


if __name__ == "__main__":
    print(multiply(2, 1))


# Best solutions:


def multiply(a, b):
    if isinstance(a, (int, float, complex)):
        if isinstance(b, (int, float, complex)):
            return a * b


def multiply(a, b):
    code = a * b
    return code
