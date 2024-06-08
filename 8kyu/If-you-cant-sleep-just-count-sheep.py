# If you can't sleep, just count sheep!!
# Task:
#
# Given a non-negative integer, 3 for example, return a string with a murmur:
# "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e.
# no negative integers.


def count_sheep(n):
    return "".join([f"{i+1} sheep..." for i in range(n)])


if __name__ == "__main__":
    print(count_sheep(2))


# Best solutions:


def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))


def count_sheep(n):
    sheep=""
    for i in range(1, n+1):
        sheep+=str(i) + " sheep..."
    return sheep


def count_sheep(n):
    return "".join("{} sheep...".format(i) for i in range(1, n+1))