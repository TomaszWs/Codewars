# The method is supposed to remove even numbers from the list and return a list
# that contains the odd numbers.
#
# However, there is a bug in the method that needs to be resolved.


def kata_13_december(lst):
    return [x for x in lst if x % 2 != 0]


if __name__ == '__main__':
    print(kata_13_december([1, 2, 2, 2, 4, 3, 4, 5, 6, 7]))


# Best solutions:


def kata_13_december(lst):
    return [x for x in lst if x%2]


def kata_13_december(lst):
    new = list()
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            new.append(lst[i])
    return new
