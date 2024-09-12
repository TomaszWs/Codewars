# Write a function which removes from string all non-digit characters and parse
# the remaining to number. E.g: "hell5o wor6ld" -> 56
#
# Function:
#
# getNumberFromString(s)


def get_number_from_string(st):
    return int("".join([char for char in st if char.isdigit()]))


if __name__ == '__main__':
    print(get_number_from_string("hell5o wor6ld"))


# Best solutions:


def get_number_from_string(string):
    return int(''.join(x for x in string if x.isdigit()))


import re


def get_number_from_string(s):
    return int(re.sub(r'\D', '', s))


def get_number_from_string(string):
    return int(''.join(filter(str.isdigit, string)))
