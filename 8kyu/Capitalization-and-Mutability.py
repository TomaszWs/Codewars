# Your coworker was supposed to write a simple helper function to capitalize a
# string (that contains a single word) before they went on vacation.
#
# Unfortunately, they have now left and the code they gave you doesn't work.
# Fix the helper function they wrote so that it works as intended (i.e. it must
# make the first character in the string upper case).
#
# The string will always start with a letter and will never be empty.
#
# Examples:
#
# "hello" --> "Hello"
# "Hello" --> "Hello" (the first letter was already capitalized)
# "a"     --> "A"


def capitalize_word(word: str) -> str:
    return word[0].upper() + word[1:]


if __name__ == '__main__':
    print(capitalize_word('word'))


# Best solutions:


def capitalizeWord(word):
    return word.capitalize()


def capitalizeWord(s):
    return s.title()
