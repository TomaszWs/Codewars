# Build a function that returns an array of integers from n to 1 where n>0.
#
# Example : n=5 --> [5,4,3,2,1]


def reverse_seq(n):
    return [i for i in range(n, 0, -1)]


if __name__ == '__main__':
    print(reverse_seq(5))


# Best solutions:


def reverseseq(n):
    return list(range(n, 0, -1))


def reverseseq(n):
    return range(n, 0, -1)


def reverse_seq(a):
    if a > 0:
        return(list(range(a, 0, -1)))
    else:
        return("pick a positive number")
