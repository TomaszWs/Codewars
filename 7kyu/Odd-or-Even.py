# Task:
#
# Given a list of integers, determine whether the sum of its elements is odd
# or even.
#
# Give your answer as a string matching "odd" or "even".
#
# If the input array is empty consider it as: [0] (array with a zero).
# Examples:
#
# Input: [0]
# Output: "even"
#
# Input: [0, 1, 4]
# Output: "odd"
#
# Input: [0, -1, -5]
# Output: "even"

import numpy as np


def odd_or_even(arr):
    if not arr:
        arr = [0]
        return "even"
    elif arr:
        if np.sum(arr) % 2 == 0:
            return "even"
        else: return "odd"


arr = [0, 1, 4]
print(odd_or_even(arr))

# Best solutions:


def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'


def oddOrEven(arr):
    """determine whether a given list of numbers is odd or even"""
    if sum(arr) % 2 == 0:
        return "even"
    else:
        return "odd"
