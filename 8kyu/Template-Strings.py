# Template Strings
# Template Strings, this kata is mainly aimed at the new JS ES6 Update
# introducing Template Strings
# Task
# Your task is to return the correct string using the Template String Feature.
# Input
# Two Strings, no validation is needed.
# Output
# You must output a string containing the two strings with the word
# ```' are '```
#
# Reference: https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/template_strings


def temple_strings(obj, feature):
    return f"{obj} are {feature}"


if __name__ == '__main__':
    print(temple_strings("Animals","Good"))


# Best solutions:


temple_strings = '{} are {}'.format


def temple_strings(obj, feature):
    return obj+" are "+feature
