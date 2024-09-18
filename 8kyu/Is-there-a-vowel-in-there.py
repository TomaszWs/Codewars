# Given an array of numbers, check if any of the numbers are the character
# codes for lower case vowels (a, e, i, o, u).
#
# If they are, change the array value to a string of that vowel.
#
# Return the resulting array.


def is_vow(inp):
    return [chr(i) if i in [ord(v) for v in "aeiou"] else i for i in inp]


if __name__ == '__main__':
    print(is_vow([118, "u",120,121,"u",98,122,"a",120,106,104,116,113,114,113,
                  120,106 ]))


# Best solutions:


def is_vow(inp):
    return [chr(n) if chr(n) in "aeiou" else n for n in inp]


def is_vow(inp):
    for i, v in enumerate(inp):
        if chr(v) in 'aeiou':
            inp[i] = chr(v)
    return inp


def is_vow(s):
    vowels = {97: 'a', 111: 'o', 117: 'u', 101: 'e', 105: 'i'}
    return [vowels.get(a, a) for a in s]
