# Given a number n, draw stairs using the letter "I", n tall and n wide, with
# the tallest in the top left.
#
# For example n = 3 result in:
#
# "I\n I\n  I"
#
# or printed:
#
# I
#  I
#   I
#
# Another example, a 7-step stairs should be drawn like this:
#
# I
#  I
#   I
#    I
#     I
#      I
#       I


def draw_stairs(n):
    return "\n".join([" " * i + "I" for i in range(n)])


if __name__ == "__main__":
    print(draw_stairs(3))


# Best solutions:


def draw_stairs(n):
    return '\n'.join(f'{" " * i}I' for i in range(n))


def draw_stairs(n):
    count = 1
    res = ""
    while count < n:
        res += "I\n" + " " * count
        count += 1
    res += "I"
    return res
