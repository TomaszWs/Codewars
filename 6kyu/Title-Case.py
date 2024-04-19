# A string is considered to be in title case if each word in the string
# is either (a) capitalised (that is, only the first letter of the word is
# in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.
#
# Write a function that will convert a string into title case, given
# an optional list of exceptions (minor words). The list of minor words will
# be given as a string with each word separated by a space. Your function
# should ignore the case of the minor words string -- it should behave
# in the same way even if the case of the minor word string is changed.
# Arguments (Haskell)
#
#     First argument: space-delimited list of minor words that must always
#     be lowercase except for the first word in the string.
#     Second argument: the original string to be converted.
#
# Arguments (Other languages)
#
#     First argument (required): the original string to be converted.
#     Second argument (optional): space-delimited list of minor words that
#     must always be lowercase except for the first word in the string.
#     The JavaScript/CoffeeScript tests will pass undefined when this
#     argument is unused.
#
# Example
#
# title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
# title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
# title_case('the quick brown fox') # should return: 'The Quick Brown Fox'


def title_case(title, minor_words=''):
    title_words = title.lower().split()
    if not minor_words:
        return " ".join(word.capitalize() for word in title_words)
    minor_words = set(minor_words.lower().split())
    for i in range(len(title_words)):
        if i == 0 or title_words[i] not in minor_words:
            title_words[i] = title_words[i].capitalize()
    return " ".join(title_words)


print(title_case('a clash of KINGS', 'a an the of'))
print(title_case('THE WIND IN THE WILLOWS', 'The In'))
print(title_case('the quick brown fox'))

# Best solutions:


def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])


def title_case(title, minor_words=''):
    title, minor_words = title.lower().split(), minor_words.lower().split()
    for i in range(len(title)):
        if i == 0 or title[i] not in minor_words:
            title[i] = title[i].capitalize()
    return ' '.join(title)


def title_case(title, minor_words=''):
    proper_title = ''

    # lowercase the entire list
    title_words = map(lambda x: x.lower(), title.split(' '))

    # split the minor word strings
    dont_cap = minor_words.split(' ')

    # always upper case the first word
    title_words = [item.capitalize() for item in title_words]

    # lower case the split minor words array
    dont_cap = [item.lower() for item in dont_cap]

    # print title_words

    # loop through the 2nd word to the end word
    for i in xrange(1, len(title_words), 1):
        # loop through the minor_words array
        for item in dont_cap:
            # if the minor word is equal to the title word, lower case it
            if item == title_words[i].lower():
                title_words[i] = title_words[i].lower()

    return " ".join(title_words)