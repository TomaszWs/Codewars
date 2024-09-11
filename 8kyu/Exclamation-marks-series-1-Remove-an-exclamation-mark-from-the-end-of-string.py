# Description:
#
# Remove an exclamation mark from the end of a string. For a beginner kata, you
# can assume that the input data is always a string, no need to verify it.
# Examples
#
# "Hi!"     ---> "Hi"
# "Hi!!!"   ---> "Hi!!"
# "!Hi"     ---> "!Hi"
# "!Hi!"    ---> "!Hi"
# "Hi! Hi!" ---> "Hi! Hi"
# "Hi"      ---> "Hi"


def remove(s):
    if len(s) == 0:
        return s
    return s[:-1] if s[-1] == "!" else s


if __name__ == '__main__':
    print(remove("Hi!"))


# Best solutions:


def remove(s):
    return s[:-1] if s.endswith('!') else s


def remove(s):
    return s.removesuffix('!')


def remove(s):
    return s[:-1] if s and s[-1] == '!' else s
