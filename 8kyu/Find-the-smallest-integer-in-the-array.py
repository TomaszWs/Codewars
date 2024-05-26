# Given an array of integers your solution should find the smallest integer.
#
# For example:
#
#     Given [34, 15, 88, 2] your solution will return 2
#     Given [34, -345, -1, 100] your solution will return -345
#
# You can assume, for the purpose of this kata, that the supplied array will not be empty.


def find_smallest_int(arr):
    return min(arr)


if __name__ == "__main__":
    print(find_smallest_int([34, 15, 88, 2]))


# Best solutions:


def findSmallestInt(arr):
    #sort array
    arr.sort()
    return arr[0]


def findSmallestInt(arr):
    smallest = []
    for i in range(0,len(arr)):
        if (arr[i] < smallest):
            smallest = arr[i]
    return smallest
