# Write a function that will check if two given characters are the same case.
#
#     If either of the characters is not a letter, return -1
#     If both characters are the same case, return 1
#     If both characters are letters, but not the same case, return 0
#
# Examples
#
# 'a' and 'g' returns 1
#
# 'A' and 'C' returns 1
#
# 'b' and 'G' returns 0
#
# 'B' and 'g' returns 0
#
# '0' and '?' returns -1


def same_case(a, b):
    if a.isalpha() and b.isalpha():
        return 1 if a.islower() and b.islower() or a.isupper() and b.isupper()\
            else 0
    else:
        return -1


if __name__ == '__main__':
    print(same_case('C', 'B'))


# Best solutions:


def same_case(a, b):
    if a.isalpha() and b.isalpha():
        return 1 if a.islower() and b.islower() or a.isupper() and b.isupper()\
            else 0
    else:
        return -1


def same_case(a, b):
    if a.isalpha() and b.isalpha():
        if (a.islower() and b.islower()) or (a.isupper() and b.isupper()):
            return 1
        else:
            return 0
    else:
        return -1


def same_case(a, b):
    c = a+b
    if not c.isalpha():
        return -1
    if c.islower() or c.isupper():
        return 1
    else:
        return 0
