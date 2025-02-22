# Implement the function generateRange which takes three arguments (start,
# stop, step) and returns the range of integers from start to stop (inclusive)
# in increments of step.
# Examples
#
# (1, 10, 1) -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# (-10, 1, 1) -> [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1]
# (1, 15, 20) -> [1]
#
# Note
#
#     start < stop
#     step > 0


def generate_range(start, stop, step):
    return [s for s in range(start, stop + 1, step)]


if __name__ == '__main__':
    print(generate_range(1, 10, 1))


# Best solutions:


def generate_range(min, max, step):
    return list(range(min, max + 1, step))


def generate_range(start, stop, step):
    return [*range(start, stop+1, step)]


def generate_range(min, max, step):
    num=[]
    for i in range(min,max+1,step):
       num.append(i)
    return num
