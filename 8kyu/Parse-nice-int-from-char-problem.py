# You ask a small girl,"How old are you?" She always says, "x years old", where
# x is a random number between 0 and 9.
#
# Write a program that returns the girl's age (0-9) as an integer.
#
# Assume the test input string is always a valid string. For example, the test
# input may be "1 year old" or "5 years old". The first character in the string
# is always a number.


def get_age(age):
    return int(age[0])


if __name__ == '__main__':
    print(get_age("2 years old"))


# Best solutions:


def get_age(age):
    for x in age:
    	if x.isdigit():
        	return int(x)


import re


def get_age(age):
    return int(re.search(r"\d+", age).group())
