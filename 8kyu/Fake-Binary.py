# Given a string of digits, you should replace any digit below 5 with '0' and
# any digit 5 and above with '1'. Return the resulting string.
#
# Note: input will never be an empty string


def fake_bin(x):
    return ''.join(['0' if int(i) < 5 else '1' for i in x ])


x = "45385593107843568"
print(fake_bin(x))

# Best solutions:


def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)


def fake_bin(x):
    result = ""
    for num in x:
        if int(num) < 5:
            result = result + "0"
        else:
            result = result + "1"
    return result


import string

def fake_bin(s):
    return s.translate(string.maketrans('0123456789', '0000011111'))