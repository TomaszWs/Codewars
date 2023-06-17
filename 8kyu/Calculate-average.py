# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.

# My solution

# def find_average(numbers):
#     i = 0
#     if numbers == []: return 0
#     else: 
#         for number in numbers:
#             i+=number
#     average = i / (len(numbers))
#     return average

# numbers = [1,2,3]
# numbers_2 = []
# x = find_average(numbers_2)
# print(x)

# Best practices

def find_average(array):
    return sum(array) / len(array) if array else 0

def find_average(array):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0