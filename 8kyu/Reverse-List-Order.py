# In this kata you will create a function that takes in a list and returns a list with the reverse order.
# Examples (Input -> Output)
#
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]


def reverse_list(l):
    return l[::-1]


print(reverse_list([1, 2, 3, 4]))


# Best solutions:


def reverse_list(l):
  """return a list with the reverse order of l"""
  return list(reversed(l))


def reverse_list(l):
  l.reverse()
  return l


def reverse_list(l):
  """ Returns reversed list. """
  return list(reversed(l))
