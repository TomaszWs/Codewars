# Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?
#
# Examples:
#
# input:    output:
# 0    ->   0
# 2    ->   5
# 3    ->   5
# 12   ->   15
# 21   ->   25
# 30   ->   30
# -2   ->   0
# -5   ->   -5
# etc.
#
# Input may be any positive or negative integer (including 0).
#
# You can assume that all inputs are valid integers.


def round_to_next5(n):
    if n%5 != 0:
        n += (5 - n % 5)
    return n

print(round_to_next5(2))


# Best solutions:


def round_to_next5(n):
    return n + (5 - n) % 5


def round_to_next5(n):
    while n%5!=0:
        n+=1
    return n


import math


def round_to_next5(n):
    # Your code here
    return math.ceil(n/5.0) * 5