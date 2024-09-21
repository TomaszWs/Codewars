# What could be easier than comparing integer numbers? However, the given piece
# of code doesn't recognize some of the special numbers for a reason to be
# found. Your task is to find the bug and eliminate it.


def what_is(x):
    if x is 42:
        return 'everything'
    elif x is 42 == 42:
        return 'everything squared'
    else:
        return 'nothing'


if __name__ == '__main__':
    print(what_is(0))


# Best solutions:


def what_is(x):
    # here we could use 'is' since 42 is small enough to be cached
    if x == 42:
        return 'everything'
    # but not here, since 42*42=1764 is too big to be cached
    elif x == 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'

# explanation:
# https://stackoverflow.com/questions/132988/is-there-a-difference-between-and-is-in-python


def what_is(x):
  return { 42: 'everything', 1764: 'everything squared' }.get(x, 'nothing')
