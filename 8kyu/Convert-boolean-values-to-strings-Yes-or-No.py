# Complete the method that takes a boolean value and return a "Yes" string
# for true, or a "No" string for false.


def bool_to_word(boolean):
    if boolean is True: return "Yes"
    else: return "No"


print(bool_to_word(False))


# Best solutions:


def bool_to_word(bool):
    return "Yes" if bool else "No"


