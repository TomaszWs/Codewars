# Given an array of seats, return the maximum number of new people
# which can be seated, as long as there is at least a gap of 2 seats
# between people.
#
#     Empty seats are given as 0.
#     Occupied seats are given as 1.
#     Don't move any seats which are already occupied, even if they
#     are less than 2 seats apart. Consider only the gaps between new
#     seats and existing seats.
#
# Examples
#
# [0, 0, 0, 1, 0, 0, 1, 0, 0, 0] ➞ 2
# // [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
#
# [0, 0, 0, 0] ➞ 2
# // [1, 0, 0, 1]
#
# [1, 0, 0, 0, 0, 1] ➞ 0
# // There is no way to have a gap of at least 2 chairs when adding
# someone else.
#
# Notes
#
#     Notice how there may be several possibilities for assigning
#     seats to people, but these cases won't affect the results.
#     All seats will be valid.


def maximum_seating(lst):
    s = lst[:]
    c = 0
    for i in range(len(s)):
        if s[i] != 0:
            continue
        l = (i - 1 < 0 or s[i - 1] == 0) and (i - 2 < 0 or s[i - 2]
            == 0)
        r = (i + 1 >=  len(s) or s[i + 1] == 0) and (i + 2 >= len(
            s) or s[i + 2] == 0)
        if l and r:
            s[i] = 1
            c += 1
    return c


if __name__ == '__main__':
    print(maximum_seating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0]))


# Best solutions:


from itertools import chain, groupby

def maximum_seating(seat_occupancies):
    return sum(max(0, (sum(1 for _ in os) - 2) // 3)
        for o, os in groupby(chain((0, 0), seat_occupancies, (0, 0)))
        if not o)


def maximum_seating(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] == 0:
            left2 = (i - 2 < 0 or lst[i - 2] == 0)
            left1 = (i - 1 < 0 or lst[i - 1] == 0)
            right1 = (i + 1 >= len(lst) or lst[i + 1] == 0)
            right2 = (i + 2 >= len(lst) or lst[i + 2] == 0)

            if left2 and left1 and right1 and right2:
                lst[i] = 1
                count += 1
    return count


import re


def maximum_seating(lst):
    return sum(1 for _ in re.finditer('(?<=00)000', f'00{ "".join(map(str,lst)) }00'))