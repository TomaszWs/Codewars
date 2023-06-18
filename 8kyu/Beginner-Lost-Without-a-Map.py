# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]

# My solution

def maps(a):
    a2 = []
    for i in a: a2.append(i*2)
    return a2

a = [1, 2, 3]
print(maps(a))

# Best practices

def maps(a):
    return [2 * x for x in a]

# ?
def maps(a):
    return map(lambda x:2*x, a)