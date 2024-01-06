# Given two integers a and b, which can be positive or negative, find the sum
# of all the integers between and including them and return it.
# If the two numbers are equal return a or b.
#
# Note: a and b are not ordered!
# Examples (a, b) --> output (explanation)
#
# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1 since both are same)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
#
# Your function should only return a number, not the explanation about how
# you get that number.


def get_sum(a, b):
    c = 0
    if a > b:
        c = b
        b = a
        a = c
    return sum(range(a, b+1))


a = 3
b = 5
print(get_sum(a, b))

# Best solutions:


def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))


def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2


def get_sum(a,b):
    if a>b : a,b = b,a
    return sum(range(a,b+1))