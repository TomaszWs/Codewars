# Oh no! I've lost my glasses, but paradoxically, I need glasses to find
# my glasses!
#
# Please help me out by showing me the index in the list which contains my
# glasses. They look like two capital Os, with at least one dash in between!
#
#     This means that both O--O and O------------O are valid glasses, but
#     not O----#--O for example!
#     Search thoroughly, you might find my glasses in places such as
#     'dustO-Odust'
#
# Examples
#
# ["phone", "O-O", "coins", "keys"] ➞ 1
#
# ["OO", "wallet", "O##O", "O----O"] ➞ 3
#
# ["O--#--O", "dustO---Odust", "more dust"] ➞ 1
#
# Notes
#
#     All lists will include one valid pair of glasses because I swear I
#     dropped them around here somewhere ...
#     All elements in the list are strings.


import re


def find_glasses(lst):
    glasses = re.compile(r"O-+O")
    for index, i in enumerate(lst):
        if glasses.search(i):
            return index


if __name__ == "__main__":
    print(find_glasses(['o-o', "O---O"]))



# Best solutions:


import re


def find_glasses(lst):
    return next( i for i,s in enumerate(lst) if re.search(r'O-+O',s) )


from itertools import count
def find_glasses(lst):
    for i in count(1):
        for j, v in enumerate(lst):
            if f"O{'-'*i}O" in v:
                return j


from re import search


def find_glasses(lst):
    return next(i for i, x in enumerate(lst) if search('O-+O', x))
