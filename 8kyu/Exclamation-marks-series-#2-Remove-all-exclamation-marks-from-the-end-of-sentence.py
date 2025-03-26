# Description:
#
# Remove all exclamation marks from the end of sentence.
# Examples
#
# "Hi!"     ---> "Hi"
# "Hi!!!"   ---> "Hi"
# "!Hi"     ---> "!Hi"
# "!Hi!"    ---> "!Hi"
# "Hi! Hi!" ---> "Hi! Hi"
# "Hi"      ---> "Hi"


def remove(st):
    return st.rstrip("!")


if __name__ == '__main__':
    print(remove("Hi!!!"))


# Best solutions:


def remove(s):
    while s and s[-1] == "!":
        s = s[:-1]
    return s


def remove(s):
    while s.endswith("!"):
        s = s[:-1:]
    return s
