# I'm new to coding and now I want to get the sum of two arrays... Actually
# the sum of all their elements. I'll appreciate for your help.
#
# P.S. Each array includes only integer numbers. Output is a number too.


def array_plus_array(arr1,arr2):
    return sum(arr1)+sum(arr2)


if __name__ == "__main__":
    print(array_plus_array([1, 2, 3], [4, 5, 6]))


# Best solutions:


def array_plus_array(arr1,arr2):
    return sum(arr1+arr2)


def array_plus_array(arr1,arr2):
    counter = 0
    for i in arr1:
        counter += i
    for i in arr2:
        counter += i
    return counter
