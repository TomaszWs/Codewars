# Create a method partition that accepts a list and a method/block. It should
# return two arrays: the first, with all the elements for which the given block
# returned true, and the second for the remaining elements.
#
# Here's a simple Ruby example:
#
# animals = ["cat", "dog", "duck", "cow", "donkey"]
# partition(animals){|animal| animal.size == 3}
#     #=> [["cat", "dog", "cow"], ["duck", "donkey"]]
#
# The equivalent in Python would be:
#
# animals = ['cat', 'dog', 'duck', 'cow', 'donkey']
# partition(animals, lambda x: len(x) == 3)
#     # (['cat', 'dog', 'cow'], ['duck', 'donkey'])
#
# If you need help, here's a reference:
#
# http://www.rubycuts.com/enum-partition


def partition(arr, classifier_method):
    true = []
    false = []

    for i in arr:
        if classifier_method(i):
            true.append(i)
        else:
            false.append(i)
    return true, false


if __name__ == '__main__':
    animals = ['cat', 'dog', 'duck', 'cow', 'donkey']
    print(partition(animals, lambda x: len(x) == 3))


# Best solutions:


def partition(list, classifier_method):
    listTrue = []
    listFalse = []
    for l in list:
        if classifier_method(l):
            listTrue.append(l)
        else:
            listFalse.append(l)
    return listTrue, listFalse


from itertools import filterfalse
def partition(lis, classifier_method):
    fir = list(filter(classifier_method, lis))
    sec = list(filterfalse(classifier_method, lis))
    return (fir, sec)


def partition(list, m):
    return ([x for x in list if m(x)],[x for x in list if not m(x)])
