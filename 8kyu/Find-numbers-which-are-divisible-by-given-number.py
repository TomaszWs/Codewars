# Complete the function which takes two arguments and returns all numbers which
# are divisible by the given divisor. First argument is an array of numbers and
# the second is the divisor.
# Example(Input1, Input2 --> Output)
#
# [1, 2, 3, 4, 5, 6], 2 --> [2, 4, 6]


def divisible_by(numbers, divisor):
    return [number for number in numbers if number % divisor == 0]


if __name__ == '__main__':
    print(divisible_by([1,2,3,4,5,6], 2))


# Best solutions:


def divisible_by(numbers, divisor):
    div_by = []
    for num in numbers:
        if num % divisor == 0:
            div_by.append(num)
    return div_by


def divisible_by(n, d):
    return list(filter(lambda x: not x%d, n))
