# Your task is to sum the differences between consecutive pairs in the array in
# descending order.
# Example
#
# [2, 1, 10]  -->  9
#
# In descending order: [10, 2, 1]
#
# Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9
#
# If the array is empty or the array has only one element the result should be
# 0 (Nothing in Haskell, None in Rust).


def sum_of_differences(arr):
    return sum(
        sorted(arr, reverse=True)[i] - sorted(arr, reverse=True)[i + 1] for i
        in range(len(arr) - 1))


if __name__ == '__main__':
    print(sum_of_differences([1, 2, 10]))


# Best solutions:


def sum_of_differences(arr):
    return max(arr) - min(arr) if arr else 0


def sum_of_differences(arr):
    arr.sort(reverse=True)
    i = 0
    res = 0
    while i < len(arr)-1:
        res += arr[i] - arr[i+1]
        i += 1
    return res


def sum_of_differences(arr):
    arr = sorted(arr, reverse=True)
    return sum(a - b for a, b in zip(arr, arr[1:]))
