# You will be given an array a and a value x. All you need to do is check
# whether the provided array contains the value.
#
# Array can contain numbers or strings. X can be either.
#
# Return true if the array contains the value, false if not.


def check(seq, elem):
    return elem in seq


if __name__ == '__main__':
    print(check([66, 101], 6))


# Best solutions:


def check(seq, elem):
    return True if elem in seq else False


def check(list, x):
    while True:
        if x in list:
            return True
        else:
            return False
    pass
