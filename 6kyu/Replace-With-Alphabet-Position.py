# Welcome.
#
# In this kata you are required to, given a string, replace every letter with
# its position in the alphabet.
#
# If anything in the text isn't a letter, ignore it and don't return it.
#
# "a" = 1, "b" = 2, etc.
# Example
#
# alphabet_position("The sunset sets at twelve o' clock.")
#
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )


def alphabet_position(text):
    filtered_text = "".join(char for char in text.lower() if char.isalpha())
    output = []
    alphabet_positions = {chr(97 + i): i + 1 for i in range(26)}
    for letter in filtered_text:
        if letter.isalpha():
            output.append(str(alphabet_positions[letter]))
    return " ".join(output)


print(alphabet_position("The sunset sets at twelve o' clock."))

# Best solutions:


def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


def alphabet_position(s):
  return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())


alphabet = 'abcdefghijklmnopqrstuvwxyz'


def alphabet_position(text):
    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alphabet.index(letter) + 1)
        return result.lstrip(' ')
