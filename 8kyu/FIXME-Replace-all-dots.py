# The code provided is supposed replace all the dots . in the specified String
# str with dashes -
#
# But it's not working properly.
# Task
#
# Fix the bug so we can all go home early.
# Notes
#
# String str will never be null.


import re


def replace_dots(s):
    return re.sub(r"\.", "-", s)


if __name__ == '__main__':
    print(replace_dots("one.two.three"))


# Best solutions:


def replace_dots(string):
    return string.replace('.', '-')
