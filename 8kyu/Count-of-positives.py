# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.
# Example

# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

# My solution

# def count_positives_sum_negatives(arr):
#     result = []
#     counter = 0
#     negative = 0
#     for i in arr:
#         if i > 0: 
#             counter+=1
#         elif i < 0: 
#             negative+=i
#     result.insert(0,counter)
#     result.insert(1,negative)
#     if not arr: result.clear()
#     return result

# Best practices

def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]

def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []