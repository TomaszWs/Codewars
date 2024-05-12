# Write a function that checks if a given string (case insensitive) is a palindrome.
#
# A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar.


def is_palindrome(s):
    return s.lower()[::-1] == s.lower()


print(is_palindrome("Abba"))


# Best solutions:


def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]


def is_palindrome(s):
    """return True if word "s" is a palindrome"""
    return s.lower() == s[::-1].lower()
