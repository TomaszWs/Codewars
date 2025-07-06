# Given a string s, write a method (function) that will return true if its a
# valid single integer or floating number or false if its not.
#
# Valid examples, should return true:
#
# isDigit("3")
# isDigit("  3  ")
# isDigit("-3.23")
#
# should return false:
#
# isDigit("3-4")
# isDigit("  3   5")
# isDigit("3 5")
# isDigit("zero")


def is_digit(s):
    try:
        float(s.strip())
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    print(is_digit())


# Best solutions:


def isDigit(string):
    return string.lstrip('-').replace('.','').isdigit()
