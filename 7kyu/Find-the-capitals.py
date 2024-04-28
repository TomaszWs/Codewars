# Instructions
#
# Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (word) as its argument, and returns an ordered list containing the indices of all capital (uppercase) letters in the string.
# Example (Input --> Output)
#
# "CodEWaRs" --> [0,3,4,6]


def capitals(word):
    return [i for i, char in enumerate(word) if char.isupper()]


print(capitals('CodEWaRs'))
print(capitals("RdgdLbDAcXLOyIAkmhqBpKYfNNgo"))


# Best solutions:


def capitals(word):
    uppers = []
    for i in range(len(word)):
        if word[i].isupper():
            uppers.append(i)
    return uppers


def capitals(word):
    return [i for i in range(len(word)) if word[i].isupper()]


def capitals(word):
    return filter(lambda x: word[x].isupper(), range(len(word)))
