# Task:
#
# Write a function that accepts two integers and returns the remainder of
# dividing the larger value by the smaller value.
#
# Division by zero should return an empty value.
# Examples:
#
# n = 17
# m = 5
# result = 2 (remainder of `17 / 5`)
#
# n = 13
# m = 72
# result = 7 (remainder of `72 / 13`)
#
# n = 0
# m = -1
# result = 0 (remainder of `0 / -1`)
#
# n = 0
# m = 1
# result - division by zero (refer to the specifications on how to handle this
# in your language)


def remainder(a,b):
    return max(a, b) % min(a, b) if min(a, b) != 0 else None


if __name__ == '__main__':
    print(remainder(17, 0))


# Best solutions:


def remainder(a,b):
    if min(a,b) == 0:
        return None
    elif a > b:
        return a % b
    else:
        return b % a


def remainder(a,b):
    if min(a,b)!=0: return max(a,b)%min(a,b)


def remainder(a:int, b:int)->int:
    '''Returns remainder of the larger of two numbers
    being divided by the smaller of two numbers.
    Returns None for divide by zero.'''
    try:
        return max(a, b) % min(a, b)
    except ZeroDivisionError:
        return None
