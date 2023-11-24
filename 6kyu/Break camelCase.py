# Complete the solution so that the function will break up camel casing, using
# a space between words.
# Example
#
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""
#
import re


def solution(s):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)


s = "camelCasing"
print(solution(s))


# Best solutions:


def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)


def solution(s):
    newStr = ""
    for letter in s:
        if letter.isupper():
            newStr += " "
        newStr += letter
    return newStr
