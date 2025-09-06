# Your collegue wrote an simple loop to list his favourite animals. But there
# seems to be a minor mistake in the grammar, which prevents the program to
# work. Fix it! :)
#
# If you pass the list of your favourite animals to the function, you should
# get the list of the animals with orderings and newlines added.
#
# For example, passing in:
#
# [ "dog", "cat", "elephant" ]
#
# will result in:
#
# "1. dog\n2. cat\n3. elephant\n"


def list_animals(animals):
    lst = ''
    for i in range(len(animals)):
        lst += str(i + 1) + '. ' + animals[i] + '\n'
    return lst


if __name__ == '__main__':
    print(list_animals([ 'dog', 'cat', 'elephant' ]))


# Best solutions:


def list_animals(animals):
    return ''.join('{}. {}\n'.format(i, x) for (i, x) in enumerate(animals, 1))
