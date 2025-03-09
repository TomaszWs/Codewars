# Write a simple regex to validate a username. Allowed characters are:
#
#     lowercase letters,
#     numbers,
#     underscore
#
# Length should be between 4 and 16 characters (both included).


import re


def validate_usr(username):
    return bool(re.fullmatch(r'[a-z0-9_]{4,16}', username))


if __name__ == '__main__':
    print(validate_usr('____'))


# Best solutions:


import re


def validate_usr(un):
    return re.match('^[a-z0-9_]{4,16}$', un) != None


import re


def validate_usr(username):
    return bool(re.match(r'^[a-z0-9_]{4,16}$', username))


