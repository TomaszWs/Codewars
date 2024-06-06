# Define a function that removes duplicates from an array of non negative numbers and returns it as a result.
#
# The order of the sequence has to stay the same.
#
# Examples:
#
# Input -> Output
# [1, 1, 2] -> [1, 2]
# [1, 2, 1, 1, 3, 2] -> [1, 2, 3]


def distinct(seq):
    dist = []
    for i in seq:
        if i not in dist:
            dist.append(i)
    return dist


if __name__ == "__main__":
    print(distinct([1, 1, 2]))


# Best solutions:


def distinct(seq):
    return sorted(set(seq), key = seq.index)


def distinct(seq):
    return list(dict.fromkeys(seq))


def distinct(seq):
    result = []
    seen = set()
    for a in seq:
        if a not in seen:
            result.append(a)
            seen.add(a)
    return result


from collections import OrderedDict
def distinct(seq):
    return list(OrderedDict.fromkeys(seq))
