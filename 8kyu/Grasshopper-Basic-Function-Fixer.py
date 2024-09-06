# Fix the function
#
# I created this function to add five to any number that was passed in to it
# and return the new value. It doesn't throw any errors but it returns the
# wrong number.
#
# Can you help me fix the function?


def add_five(num):
    return num + 5


if __name__ == '__main__':
    print(add_five(5))


# Best solutions:


def add_five(num):
    total = num + 5
    return total
