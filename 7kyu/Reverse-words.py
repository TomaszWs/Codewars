# Complete the function that accepts a string parameter, and reverses each word
# in the string. All spaces in the string should be retained.
# Examples
#
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"
#


def reverse_words(text):
    words = text.split(' ')
    reversed_words = [word[::-1] for word in words]
    reversed_text = ' '.join(reversed_words)
    return reversed_text


text = "double  spaced  words"
print(reverse_words(text))

# Best solutions:

def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))

