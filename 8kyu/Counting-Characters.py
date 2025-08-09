# Define a method named countCharOccurrences or count_char_occurrences that
# accepts a string and a char as inputs and returns the number of times the
# char occurs in the string as an int.


def count_char_occurrences(strng, char):
    return strng.count(char)


if __name__ == '__main__':
    print(count_char_occurrences("missippi", 'i'))


# Best solutions:


def count_char_occurrences(strng, char):
    count = 0

    for s in strng:
        if (char in s):
            count += 1

    return count


def count_char_occurrences(strng, char):
    list = []
    count = 0
    for i in strng:
        if i == char:
            count += 1
    return count

