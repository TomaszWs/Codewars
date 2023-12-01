# The goal of this exercise is to convert a string to a new string where each
# character in the new string is "(" if that character appears only once in
# the original string, or ")" if that character appears more than once in the
# original string. Ignore capitalization when determining if a character is a
# duplicate.
# Examples
#
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("
#
# Notes
#
# Assertion messages may be unclear about what they display in some languages.
# If you read "...It Should encode XXX", the "XXX" is the expected result,
# not the input!


def duplicate_encode(word):
    dict = {}
    code = ""
    word = word.lower()
    for char in word:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    for char in word:
        if dict[char] > 1:
            code += ')'
        else:
            code += '('
    return code


word = "recede"
print(duplicate_encode(word))

# Best solutions:


def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


from collections import Counter

def duplicate_encode(word):
    word = word.lower()
    counter = Counter(word)
    return ''.join(('(' if counter[c] == 1 else ')') for c in word)


