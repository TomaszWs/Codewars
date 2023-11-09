# Take 2 strings s1 and s2 including only letters from a to z. Return a new
# sorted string, the longest possible, containing distinct letters - each
# taken only once - coming from s1 or s2.
# Examples:
#
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"
#
# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"


def longest(a1, a2):
    sorted_s = a1 + a2
    sorted_s = ''.join(sorted(set(sorted_s)))
    return sorted_s


a1 = "aehrty"
a2 = "aehrsty"
print(longest(a1, a2))


# Best solutions

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))


def longest(s1, s2):
    return ''.join(sorted((set(s1+s2))))