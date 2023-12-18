# Count the number of divisors of a positive integer n.
#
# Random tests go up to n = 500000.
# Examples (input --> output)
#
# 4 --> 3 // we have 3 divisors - 1, 2 and 4
# 5 --> 2 // we have 2 divisors - 1 and 5
# 12 --> 6 // we have 6 divisors - 1, 2, 3, 4, 6 and 12
# 30 --> 8 // we have 8 divisors - 1, 2, 3, 5, 6, 10, 15 and 30
#
# Note you should only return a number, the count of divisors. The numbers
# between parentheses are shown only for you to see which numbers are counted
# in each case.


def divisors(n):
    div = 1
    for i in range(2,n+1):
        if n % i == 0:
            div += 1
    return div


n = 30
print(divisors(n))

# Best solutions:


def divisors(n):
    return len([l_div for l_div in range(1, n + 1) if n % l_div == 0]);


# For Beginners.

# Time: 11724ms
# it's slow because use isinstance
def divisors5(n):
    return len(list(filter(lambda e: isinstance(e, int), [x if n % x == 0 else None for x in range(1, n + 1)])))


# Time: 7546ms
# it's little fast because just directly check boolean
def divisors4(n):
    return len(list(filter(lambda e: e, [True if n % x == 0 else False for x in range(1, n + 1)])))


# Time: 4731ms
# in python True is evaluate as 1
# so when prime factorization just set True and sum will return count
def divisors3(n):
    return sum([True if n % x == 0 else False for x in range(1, n + 1)])


# Time: 3675ms
# even don't need return true, cause comparison operator will return boolean
def divisors2(n):
    return sum([n % x == 0 for x in range(1, n + 1)])


# same time with above but make short code via lambda expression
divisors = lambda n: sum([n % x == 0 for x in range(1, n + 1)])