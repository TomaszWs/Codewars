# Summation

# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

# For example (Input -> Output):

# 2 -> 3 (1 + 2)
# 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)

# My solution

def summation(num):
    l = [1]
    n = 1
    while n < num:
        n+=1
        l.append(n)
    result = 0
    for i in l:
        result = result + i
    return result

# Best practices

def summation(num):
    return sum(xrange(num + 1))

def summation(num):
    return sum(range(1,num+1))