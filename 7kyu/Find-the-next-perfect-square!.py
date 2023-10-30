# You might know some pretty large perfect squares. But what about the NEXT
# one?

# Complete the findNextSquare method that finds the next integral perfect
# square after the one passed as a parameter. Recall that an integral perfect
# square is an integer n such that sqrt(n) is also an integer.
#
# If the parameter is itself not a perfect square then -1 should be returned.
# You may assume the parameter is non-negative.

# Examples:(Input --> Output)
#
# 121 --> 144
# 625 --> 676
# 114 --> -1 since 114 is not a perfect square

import math


def find_next_square(sq):
    if isinstance(sq, int):
        nsq = math.sqrt(sq)
        is_integer = nsq == int(nsq)
        if is_integer:
            nsq += 1
            nsq = nsq*nsq
            return int(nsq)
        else: return -1
    else: return -1


sq = input()
sq = int(sq)
result = find_next_square(sq)
print(result)

# Best solutions

# def find_next_square(sq):
#     root = sq ** 0.5
#     if root.is_integer():
#         return (root + 1)**2
#     return -1
#
# def find_next_square(sq):
#     x = sq**0.5
#     return -1 if x % 1 else (x+1)**2
#
# import math
# def find_next_square(sq):
#     return (math.sqrt(sq) + 1) ** 2 if (math.sqrt(sq)).is_integer() else -1
