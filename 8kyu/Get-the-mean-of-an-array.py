# It's the academic year's end, fateful moment of your school report. The
# averages must be calculated. All the students come to you and entreat you to
# calculate their average for them. Easy ! You just need to write a script.
#
# Return the average of the given array rounded down to its nearest integer.
#
# The array will never be empty.


from numpy import mean


def get_average(marks):
    return int(mean(marks))


if __name__ == '__main__':
    print(get_average([1, 5, 87, 45, 8, 8]))


# Best solutions:


def get_average(marks):
    return sum(marks) // len(marks)


import math
import numpy
def get_average(marks):
    number =  numpy.average(marks)
    return math.floor(number)
