# Consider an array/list of sheep where some sheep may be missing from their
# place. We need a function that counts the number of sheep present in the
# array (true means present).
#
# For example,
#
# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
#
# The correct answer would be 17.
#
# Hint: Don't forget to check for bad values like null/undefined


def count_sheeps(sheep):
  return sheep.count(True)


if __name__ == '__main__':
    sheep = [True, True, True, False,
              True, True, True, True,
              True, False, True, False,
              True, False, False, True,
              True, True, True, True,
              False, False, True, True]

    print(count_sheeps(sheep))


# Best solutions:


def count_sheeps(array_of_sheep):
  count = 0
  for sheep in array_of_sheep:
      if sheep:
          count += 1
  return count


def count_sheeps(sheep):
  return len([x for x in sheep if x])
