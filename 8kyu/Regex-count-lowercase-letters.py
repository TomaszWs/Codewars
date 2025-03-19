# Your task is simply to count the total number of lowercase letters in a
# string.
# Examples
#
# "abc" ===> 3
#
# "abcABC123" ===> 3
#
# "abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 3
#
# "" ===> 0;
#
# "ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 0
#
# "abcdefghijklmnopqrstuvwxyz" ===> 26


def lowercase_count(strng):
    return len([i for i in strng if i.islower()])


if __name__ == '__main__':
    print(lowercase_count("abcABC123"))


# Best solutions:


def lowercase_count(strng):
    return sum(a.islower() for a in strng)


import re


def lowercase_count(string):
    return len(re.findall('[a-z]',string))


def lowercase_count(str):
    return sum(1 for c in str if c.islower())
