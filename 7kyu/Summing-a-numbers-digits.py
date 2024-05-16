# Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.
#
# For example: (Input --> Output)
#
# 10 --> 1
# 99 --> 18
# -32 --> 5
#
# Let's assume that all numbers in the input will be integer values.


def sum_digits(number):
    return sum([int(i) for i in str(abs(number))])


print(sum_digits(-32))


# Best solutions:


def sumDigits(number):
    return sum(int(d) for d in str(abs(number)))


def sum_digits(number):
    return sum(map(int, str(abs(number))))


def sumDigits(number):
    number = abs(number)
    return_number = 0

    while number > 0:
        return_number += number % 10
        number = int(number / 10)

    return return_number
