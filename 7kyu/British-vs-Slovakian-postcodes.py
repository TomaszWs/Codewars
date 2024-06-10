# Task
#
# Write a function called which_postcode/whichPostcode that takes a string,
# and determines whether it represents a British or Slovakian postcode. If the
# string is a valid British postcode, return "GB". If it's a valid Slovakian
# postcode, return "SK". If the input is neither a valid British nor a valid
# Slovakian postcode, return "Not valid".
#
# Leading and trailing spaces should be ignored, but if there are spaces in
# wrong place in the middle of the postcode, then it is invalid.
#
# The input will always be a valid British postcode, a valid Slovakian postcode
# or an invalid postcode.
# British Postcodes
#
# To be considered valid, a British postcode must follow the rules below:
#
#     Consists a mix of letters and numbers, seperated to two segments by a
#     single space.
#     First segment must start with either 1 or 2 letters, followed by 1 or 2
#     numbers. Example: G4, G40, DN4 or DN11
#     Second segment must start with a digit, followed by 2 letters.
#     Example: 1AB
#
# British postcodes are not case-sensitive, so Se21 7aA is a valid postcode.
# Slovakian Postcodes
#
#     Consists of 5 numbers, where the first 3 are seperated by a space from
#     the last 2 numbers. Example: 123 45.
#
# Examples
# Valid British postcodes:
#
#       G4 7AH
#     G12 8NU
#     Dn1 1aA
#     SE21 7AA
#
# Valid Slovakian postcodes:
#
#      040 01
#     810 08
#     984 59
#
# Invalid postcodes:
#
#     0765 820 - Should only have 3 numbers in the first segment, 2 numbers
#     in the second segment
#     SE 21 7AA - Should only contain 2 segments
#     070  08 - Should have single space separating the two segments, not
#     double space


import re # you can use re, but do not have to


def which_postcode(postcode):
    postcode = postcode.strip()
    if re.search("^([a-zA-Z]{1,2}\d{1,2}\s\d[a-zA-Z]{2})$", postcode):
        return "GB"
    elif re.search("^(\d{3}\s\d{2})$", postcode):
        return "SK"
    else: return "Not valid"


if __name__ == "__main__":
    print(which_postcode("040 01"))


# Best solutions:


import re
RULES = {
    'GB': re.compile(r'(?i)[A-Z]{1,2}\d\d? \d[A-Z]{2}'),
    'SK': re.compile(r'\d{3} \d\d')
}


def which_postcode(postcode):
    return next((p for p, r in RULES.items() if r.fullmatch(postcode.strip())), 'Not valid')


import re


def which_postcode(postcode):
    m = re.fullmatch("(?P<SK>\d{3} \d\d)|(?P<GB>[A-Z]{1,2}\d{1,2} \d[A-Z]{2})", postcode.strip(), flags=re.I)
    return m.lastgroup if m else 'Not valid'


import re


def which_postcode(postcode):
    if re.match("^\s*[a-z]{1,2}\d\d? \d[a-z]{2}\s*$", postcode, re.IGNORECASE): return "GB"
    if re.match("^\s*\d{3} \d{2}\s*$", postcode): return "SK"
    return "Not valid"
