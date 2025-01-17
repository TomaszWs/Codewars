# Given a sequence of items and a specific item in that sequence, return the
# item immediately following the item specified. If the item occurs more than
# once in a sequence, return the item after the first occurence. This should
# work for a sequence of any type.
#
# When the item isn't present or nothing follows it, the function should return
# nil in Clojure and Elixir, Nothing in Haskell, undefined in JavaScript, None
# in Python.
#
# next_item([1, 2, 3, 4, 5, 6, 7], 3) # => 4
# next_item(['Joe', 'Bob', 'Sally'], 'Bob') # => "Sally"


def next_item(xs, item):
    if item in xs:
        i = xs.index(item)
        if i + 1 < len(xs):
            return xs[i + 1]
    return None


if __name__ == '__main__':
    print(next_item(['a', 'b', 'c'], 'd'))


# Best solutions:


def next_item(xs, item):
    it = iter(xs)
    for x in it:
        if x == item:
            break
    return next(it, None)


def next_item(xs, item):
  it = iter(xs)
  next(iter(x for x in it if x == item), None)
  return next(it, None)


def next_item(xs, item):
    found = None
    for x in xs:
        if found:
            return x
        if x == item:
            found = True
    return None

