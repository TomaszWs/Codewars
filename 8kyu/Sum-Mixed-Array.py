# Given an array of integers as strings and numbers, return the sum of the
# array values as if all were numbers.
#
# Return your answer as a number.


def sum_mix(arr):
    return sum(int(el) for el in arr)


if __name__ == "__main__":
    print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]))


# Best solutions:


def sum_mix(arr):
    return sum(map(int, arr))


def sum_mix(arr):
    somme = 0
    for i in arr:
        somme += int(i)
    return somme;
