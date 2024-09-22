# Clock shows h hours, m minutes and s seconds after midnight.
#
# Your task is to write a function which returns the time since midnight in
# milliseconds.
# Example:
#
# h = 0
# m = 1
# s = 1
#
# result = 61000
#
# Input constraints:
#
#     0 <= h <= 23
#     0 <= m <= 59
#     0 <= s <= 59


def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1000


if __name__ == '__main__':
    print(past(0,1,1))


# Best solutions:


def past(h, m, s):
    # Good Luck!
    return 3600000 * h + 60000 * m + 1000 * s


def past(h, m, s):
    if 0 <= h <= 23 or 0 <= m <= 59 or 0 <= s <= 59:
        x = h * 3600000
        y = m * 60000
        z = s * 1000
        total = x + y + z
        return(total)
    else:
        return("Please input an hour between 0 and 23 and a minute or second inbetween 0 and 59.")


def past(h, m, s):
    return (s + (m + h * 60) * 60) * 1000