# Basic regex tasks. Write a function that takes in a numeric code of any
# length. The function should check if the code begins with 1, 2, or 3 and
# return true if so. Return false otherwise.
#
# You can assume the input will always be a number.


import re


def validate_code(code):
    return True if re.search("^[123]", str(code)) else False


if __name__ == '__main__':
    print(validate_code(123))


# Best solutions:


def validate_code(code):
    return str(code).startswith(('1', '2', '3'))


def validate_code(code):
    return str(code)[0] in '123'


def validate_code(code):
    import re
    return bool(re.match(r"^[123]\d*$",str(code)))
