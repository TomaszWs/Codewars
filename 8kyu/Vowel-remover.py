# Create a function called shortcut to remove the lowercase vowels
# (a, e, i, o, u ) in a given string.
# Examples
#
# "hello"     -->  "hll"
# "codewars"  -->  "cdwrs"
# "goodbye"   -->  "gdby"
# "HELLO"     -->  "HELLO"
#
#     don't worry about uppercase vowels
#     y is not considered a vowel for this kata


def shortcut( s ):
    return "".join([l for l in s if l not in "aeiou"])


print(shortcut("hello"))


# Best solutions:


def shortcut( s ):
    for vowel in "aeiou":
        s = s.replace(vowel, "")
    return s


import re


def shortcut( s ):
    return re.sub('[aoeui]', '', s)


def shortcut(s):
    for i in ["a","e","i","o","u"]:
        if i in s:
            s = s.replace(i,"")

    return(s)