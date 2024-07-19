# Given 2 strings, a and b, return a string of the form short+long+short, with
# the shorter string on the outside and the longer string on the inside. The
# strings will not be the same length, but they may be empty ( zero length ).
#
# Hint for R users:
#
#     The length of string is not always the same as the number of characters
#
# For example: (Input1, Input2) --> output
#
# ("1", "22") --> "1221"
# ("22", "1") --> "1221"
#
# ShortLongShort.solution("1", "22"); // returns "1221"
# ShortLongShort.solution("22", "1"); // returns "1221"


def solution(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b


if __name__ == "__main__":
    print(solution("1", "22"))


# Best solutions:


def solution(a, b):
    return a+b+a if len(a)<len(b) else b+a+b


def solution(a, b):
    return '{0}{1}{0}'.format(*sorted((a, b), key=len))


def solution(a, b):
    short, long = sorted((a, b), key=len)
    return short + long + short
