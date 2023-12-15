# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the
# average student in your class.
#
# You receive an array with your peers' test scores. Now calculate the average
# and compare your score!
#
# Return True if you're better, else False!
# Note:
#
# Your points are not included in the array of your class's points. For
# calculating the average point you may add your point to the given array!
import numpy as np


def better_than_average(class_points, your_points):
    if your_points > np.average(class_points): return True
    else: return False


class_points = [2, 3]
your_points = 5
print(better_than_average(class_points,your_points))

# Best solutions:


def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)


def better_than_average(class_points, your_points):
    average = (sum(class_points) + your_points) / (len(class_points) + 1)
    return your_points > average


import statistics
def better_than_average(class_points, your_points):
    return your_points > statistics.mean(class_points)