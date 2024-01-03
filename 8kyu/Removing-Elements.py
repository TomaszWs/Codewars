# Take an array and remove every second element from the array. Always keep
# the first element and start removing with the next element.
# Example:
#
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...]
#   --> ["Keep", "Keep", "Keep", ...]
#
# None of the arrays will be empty, so you don't have to worry about that!


def remove_every_other(my_list):
    return [element for i, element in enumerate(my_list) if i % 2 == 0]


my_list = ["Keep", "Remove", "Keep", "Remove", "Keep", ...]
print(remove_every_other(my_list))

# Best solutions:


def remove_every_other(my_list):
    return my_list[::2]


def remove_every_other(my_list):
    r = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            r.append(my_list[i])
    return r


def remove_every_other(my_list):
    return [v for c,v in enumerate(my_list) if not c%2]
