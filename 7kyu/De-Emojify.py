# Inspired by the emojify custom Python module.
#
# You are given a string made up of chains of emotes separated by 1 space each,
# with chains having 2 spaces in-between each.
#
# Each emote represents a digit:
#
# :)  | 0
# :D  | 1
# >(  | 2
# >:C | 3
# :/  | 4
# :|  | 5
# :O  | 6
# ;)  | 7
# ^.^ | 8
# :(  | 9
#
# Each emote chain represents the digits of the ASCII/Unicode code for a
# character, e.g. :( ;) is 97, which is the ASCII code for 'a'.
#
# Given a such string of emotes, find the string it represents. Example:
#
# ':D :) :/  :D :) :|' is 2 chains: ':D :) :/' and ':D :) :|'.
#
# These represent ASCII codes 104 and 105 respectively, translating to 'hi'.
#
# Input will always be valid. Chains may start with leading zeroes; these are
# valid and do not change the chain's value.
#
# hobovsky if you're reading this, you're welcome for the emoji kata idea


def deemojify(emote_string):
    emoji = {
        ":)" : 0,
        ":D" : 1,
        ">(" : 2,
        ">:C": 3,
        ":/": 4,
        ":|": 5,
        ":O": 6,
        ";)": 7,
        "^.^": 8,
        ":(": 9
    }
    parts = emote_string.split("  ")
    return "".join([chr(int("".join([str(emoji[e]) for e in part.split(" ")]))) for part in parts])


if __name__ == "__main__":
    print(deemojify(';) >(  :D :) :D  :D :) ^.^  :D :) ^.^  :D :D :D  >:C >(  :D :D :(  :D :D :D  :D :D :/  :D :) ^.^  :D :) :)  >:C >:C'))


# Best solutions:


def deemojify(string):
    digits = {
        ':)': '0',
        ':D': '1',
        '>(': '2',
        '>:C': '3',
        ':/': '4',
        ':|': '5',
        ':O': '6',
        ';)': '7',
        '^.^': '8',
        ':(': '9',
    }
    result = ''
    for group in string.split('  '):
        number = ''
        for emoji in group.split(' '):
            number += digits[emoji]
        result += chr(int(number))
    return result


def deemojify(string):
    a = [':)', ':D', '>(', '>:C', ':/', ':|', ':O', ';)', '^.^', ':(']
    c = string.split("  ")
    for i in range(len(c)):
        c[i]=c[i].split()
        for j in range(len(c[i])):
            c[i][j] = str(a.index(c[i][j]))
        c[i] = chr(int(''.join(c[i])))
    return''.join(c)


