# Description:
#
# Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.
# Examples
#
# replace("Hi!") === "H!!"
# replace("!Hi! Hi!") === "!H!! H!!"
# replace("aeiou") === "!!!!!"
# replace("ABCDE") === "!BCD!"


from re import sub


def replace_exclamation(st):
    return sub("[AEIOUaeiou]", "!", st)


if __name__ == '__main__':
    print(replace_exclamation("aeiou"))


# Best solutions:


def replace_exclamation(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)


def replace_exclamation(s):
    return s.translate(str.maketrans('aeiouAEIOU', '!' * 10))


def replace_exclamation(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for a in s:
        if a in vowels:
            s = s.replace(a,'!')
    print(s)
    return s
