# Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):
#
# Example: (Input1, Input2 -->Output)
#
# "4",  "5" --> "9"
# "34", "5" --> "39"
# "", "" --> "0"
# "2", "" --> "2"
# "-5", "3" --> "-2"
#
# Notes:
#
#     If either input is an empty string, consider it as zero.
#
#     Inputs and the expected output will never exceed the signed 32-bit integer limit (2^31 - 1)


def sum_str(a, b):
    if a == "" and b == "":
        return "0"
    elif b == "":
        return str(int(a) + 0)
    elif a == "":
        return str(int(b) + 0)
    else:
        return str(int(a) + int(b))


print(sum_str("",  ""))


# Best solutions:


def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))


def sum_str(a, b):
    return str(int('0' + a) + int('0' + b))


def sum_str(a, b):
    print(a, b)
    if a == "" or a == None: a = "0"
    if b == "" or b == None: b = "0"
    return str(int(a)+int(b))