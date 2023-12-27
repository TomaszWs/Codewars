# You will be given a list of strings. You must sort it alphabetically
# (case-sensitive, and based on the ASCII values of the chars) and then return
# the first value.
#
# The returned value must be a string, and have "***" between each
# of its letters.
#
# You should not remove or add elements from/to the array.


def two_sort(array):
    array.sort()
    return "***".join([char for char in array[0]])


array = ["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows",
         "perhaps"]
print(two_sort(array))

# Best solutions:


def two_sort(lst):
    return '***'.join(min(lst))


def two_sort(arr):
    return '***'.join(sorted(arr)[0])


def two_sort(a):
    a = sorted(a)
    result = "***".join(a[0])
    return result