# Write a function to split a string and convert it into an array of words.
# Examples (Input ==> Output):
#
# "Robin Singh" ==> ["Robin", "Singh"]
#
# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they",
# "are", "my", "favorite"]


def string_to_array(s):
    return s.split() if s else [""]


if __name__ == '__main__':
    print(string_to_array(""))


# Best solutions:


def string_to_array(string):
    return string.split(" ")


def string_to_array(s):
    return s.split(' ')


def string_to_array(string):
    return string.split() or ['']
