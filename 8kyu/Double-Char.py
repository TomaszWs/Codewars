# Given a string, you have to return a string in which each character
# (case-sensitive) is repeated once.
# Examples (Input -> Output):
#
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "
#
# Good Luck!


def double_char(s):
    s2 = []
    for i in s:
        s2.append(i * 2)
    return "".join(s2)


if __name__ == "__main__":
    print(double_char("String"))


# Best solutions:


def double_char(s):
    return ''.join(c * 2 for c in s)


def double_char(s):
    res = ''
    for i in s:
        res += i*2
    return res
