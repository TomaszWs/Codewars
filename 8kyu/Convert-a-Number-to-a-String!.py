# We need a function that can transform a number (integer) into a string.
#
# What ways of achieving this do you know?
# Examples (input --> output):
#
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"


def number_to_string(num):
    num_2 = str(num)
    return num_2


num = int(input())
num_2 = number_to_string(num)
print(type(num_2))

# Best solutions


def number_to_string(num):
    return str(num)


def number_to_string(num):
    try:
        return str(num)
    except:
        return None