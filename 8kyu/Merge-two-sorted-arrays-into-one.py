# You are given two sorted arrays that both only contain integers. Your task
# is to find a way to merge them into a single one, sorted in asc order.
# Complete the function mergeArrays(arr1, arr2), where arr1 and arr2 are the
# original sorted arrays.
#
# You don't need to worry about validation, since arr1 and arr2 must be arrays
# with 0 or more Integers. If both arr1 and arr2 are empty, then just return
# an empty array.
#
# Note: arr1 and arr2 may be sorted in different orders. Also arr1 and arr2
# may have same integers. Remove duplicated in the returned result.
# Examples (input -> output)
#
# * [1, 2, 3, 4, 5], [6, 7, 8, 9, 10] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# * [1, 3, 5, 7, 9], [10, 8, 6, 4, 2] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# * [1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12] -> [1, 2, 3, 4, 5, 7, 9, 10, 11, 12]


def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))


if __name__ == "__main__":
    print(merge_arrays([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))


# Best solutions:


def merge_arrays(arr1, arr2):
  for arr in (arr1, arr2):
    if arr[0] > arr[-1]:
      arr.reverse()
  res = []
  i = 0
  k = 0
  while not(i >= len(arr1) and k >= len(arr2)):
    left = arr1[i] if i < len(arr1) else float("inf")
    right = arr2[k] if k < len(arr2) else float("inf")
    res_last = res[-1] if res else None
    if left <= right:
      res_last != left and res.append(left)
      i += 1
    else:
      res_last != right and res.append(right)
      k += 1
  return res


def merge_arrays(arr1, arr2):
    return sorted(set(arr1) | set(arr2))
