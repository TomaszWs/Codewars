# The main idea is to count all the occurring characters in a string.
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
#
# What if the string is empty? Then the result should be
# empty object literal, {}.


def count(s):
    if s == '': return {}
    else:
        dict = {}
        for char in s:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] +=1
        return dict


s = "aba"
print(count(s))

# Best solution:


from collections import Counter

def count(string):
    return Counter(string)


def count(string):
    return {i: string.count(i) for i in string}


def count(s):
    return {x:s.count(x) for x in set(s)}