# You get an array of numbers, return the sum of all of the positives ones.
#
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
#
# Note: if there is nothing to sum, the sum is default to 0.


def positive_sum(arr):
    return sum([number for number in arr if number > 0])


if __name__ == "__main__":
    print(positive_sum([1,-4,7,12]))


# Best solutions:


def positive_sum(arr):
    return sum(x for x in arr if x > 0)


def positive_sum(arr):
    return sum(filter(lambda x: x > 0,arr))


def positive_sum(arr):
    sum = 0
    for e in arr:
        if e > 0:
            sum = sum + e
    return sum
