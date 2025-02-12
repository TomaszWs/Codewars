# When provided with a letter, return its position in the alphabet.
#
# Input :: "a"
#
# Output :: "Position of alphabet: 1"
#
# Note: Only lowercased English letters are tested


def position(letter):
    return f"Position of alphabet: {ord(letter) - ord('a') + 1}"


if __name__ == '__main__':
    print(position("a"))


# Best solutions:


def position(alphabet):
    return "Position of alphabet: {}".format(ord(alphabet) - 96)
