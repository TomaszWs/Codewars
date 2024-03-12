# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
#
# The input string will only consist of lower case letters and/or spaces.


def get_count(sentence):
    return sum(1 for char in sentence if char in "aeiou")


print(get_count("the sunset sets at twelve o clock"))


# Best solutions:


def getCount(s):
    return sum(c in 'aeiou' for c in s)


def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels + 1
    return num_vowels
