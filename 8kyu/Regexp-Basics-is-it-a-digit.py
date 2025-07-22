# Implement String#digit? (in Java StringUtils.isDigit(String)), which should
# return true if given object is a single digit (0-9), false otherwise.


def is_digit(n):
    return n.isdigit() and len(n) == 1


if __name__ == '__main__':
    print(is_digit(" "))


# Best solutions:


import re


def is_digit(n):
    return bool(re.match("\d\Z", n))


import re


def is_digit(n):
    return bool(re.fullmatch(r'\d', n))