# Write a function that returns a string in which firstname is swapped with last name.
#
# Example(Input --> Output)
#
# "john McClane" --> "McClane john"


def name_shuffler(str_):
    name = str_.split(" ")
    name.reverse()
    return " ".join(name)


print(name_shuffler("john McClane"))


# Best solutions:


def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])


def name_shuffler(str_):
    [first, last] = str_.split()
    return last + " " + first


def name_shuffler(s):
    return ' '.join(reversed(s.split()))
