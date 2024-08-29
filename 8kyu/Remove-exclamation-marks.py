# Write function RemoveExclamationMarks which removes all exclamation marks
# from a given string.


def remove_exclamation_marks(s):
    return "".join([char for char in s if char != "!"])


if __name__ == '__main__':
    print(remove_exclamation_marks("Hello World!"))


# Best solutions:


def remove_exclamation_marks(s):
    return s.replace('!', '')


def remove_exclamation_marks(s):
    """ return s.replace('!', '') """
    new_s = ''
    for i in s:
        if i != '!':
            new_s += i
    return new_s
