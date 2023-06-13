# Very simple, given an integer or a floating-point number, find its opposite.

# Examples:

# 1: -1
# 14: -14
# -34: 34

# My solution

def opposite(number):
  opposite_number = number*(-1)
  return opposite_number


print('Enter number:')
number = float(input())
opposite = opposite(number)
print(opposite)

# Best practices

def opposite(number):
    return -number

def opposite(number):
  return number * -1