# A numeral system is a way of writing numbers using a specific set of
# digits: for example, the decimal system (also called base-10), which
# is the most commonly used numeral system worldwide, uses the digits
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 to represent numbers. There is also the
# binary system (also called base-2), which uses the digits 0 and 1.
#
# For digits that are bigger than 9, the English alphabet is used: 'A'
# is used for the number 10 in bases higher than 10. This goes all the
# way to 'Z' in base-36.
#
# The largest digit allowed in a certain base is always 1 smaller than
# this base.
#
# You need to write a function that checks whether all of the digits
# of a non-negative integer number are a part of the specified base:
# for example, the number 17253 is valid for base-8, because this base
# contains the digits 0, 1, 2, 3, 4, 5, 6, 7, but the number 19823 is
# not valid for this base, because it contains the digits 9 and 8
# which are not a part of base-8.
#
# Note: numbers will be checked against bases from 2 to 36.
# For digits > 9 (A, B, etc.) such digits will always be uppercase.
# The function should return a boolean: true for numbers that are
# valid for a specified numeral system and false otherwise.


def validate_base(num: str, base: int) -> bool:
    return all(i in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:base] for i in num)


if __name__ == '__main__':
    print(validate_base('7623',  8))


# Best solutions:


from string import ascii_uppercase, digits

BASE = digits + ascii_uppercase

def validate_base(num, base):
    return set(num)<=set(BASE[:base])


def validate_base(num, base):
    return max(num) <= "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[base-1]


def validate_base(num: str, base: int) -> bool:
    # print(base)
    a_z = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
        "G": 16,
        "H": 17,
        "I": 18,
        "J": 19,
        "K": 20,
        "L": 21,
        "M": 22,
        "N": 23,
        "O": 24,
        "P": 25,
        "Q": 26,
        "R": 27,
        "S": 28,
        "T": 29,
        "U": 30,
        "V": 31,
        "W": 32,
        "X": 33,
        "Y": 34,
        "Z": 35
    }

    for i in num:
        if a_z[i] >= base:
            result = False
            break
        else:
            result = True
    return result
