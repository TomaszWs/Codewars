# Write a function that merges two sorted arrays into a single one. The arrays
# only contain integers. Also, the final outcome must be sorted and not have
# any duplicate.


def merge_arrays(first, second):
    return sorted(set(first + second))


if __name__ == '__main__':
    print(merge_arrays([2, 4, 8], [2, 4, 6]))


# Best solutions:


def merge_arrays(first, second):
    working = []
    for e in first:
        if e not in working:
            working.append(e)
    for i in second:
        if i not in working:
            working.append(i)
    return sorted(working)
