# I would like to be able to pass an array with two elements to my swapValues
# function to swap the values. However it appears that the values aren't
# changing.
#
# Can you figure out what's wrong here?


def swap_values(args):
    args[0], args[1] = args[1], args[0]
    return args


if __name__ == '__main__':
    print(swap_values([2, 1]))


# Best solutions:


def swap_values(args):
    args[0], args[1] = args[1], args[0]


def swap_values(arr):
    arr.reverse()
