# This time no story, no theory. The examples below show you how to write
# function accum:
# Examples:
#
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
#
# The parameter of accum is a string which includes only letters from a..z
# and A..Z.


def accum(s):
    result = ""
    for i, char in enumerate(s):
        result += char.upper()+char.lower()*i
        if i < len(s) - 1:
            result += "-"
    return result


s = "abcd"
print(accum(s))

# Best solutions:


def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


def accum(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))


def accum(s):
    output = ""
    for i in range(len(s)):
        output+=(s[i]*(i+1))+"-"
    return output.title()[:-1]