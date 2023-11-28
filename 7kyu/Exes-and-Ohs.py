# Check to see if a string has the same amount of 'x's and 'o's. The method
# must return a boolean and be case insensitive. The string can contain any
# char.
#
# Examples input/output:
#
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false
#


def xo(s):
    dict  = {"o":0, "x":0}
    s = s.lower()
    for char in s:
        if char in dict:
            dict[char] += 1
    if dict["o"] == dict["x"]:
        return True
    else: return False


s = "xooxx"
print(xo(s))

# Best solutions:


def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


def xo(s):
    return s.lower().count('x') == s.lower().count('o')