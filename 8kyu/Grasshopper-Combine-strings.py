# Combine strings function
#
# Create a function named (combine_names) that accepts two parameters
# (first and last name). The function should return the full name.
#
# Example:
#
# combine_names('James', 'Stevens')
#
# returns:
#
# 'James Stevens'


def combine_names(first_name, last_name):
    return first_name + " " + last_name


if __name__ == "__main__":
    print(combine_names('James', 'Stevens'))


# Best solutions:


def combine_names(*args):
    return ' '.join(args)


def combine_names(first, second):
    return '{} {}'.format(first, second)


def combine_names(first_name: str, last_name: str) -> str:
    return f'{first_name} {last_name}'
