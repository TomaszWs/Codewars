# Triple Trouble
#
# Create a function that will return a string that combines all of the letters
# of the three inputed strings in groups. Taking the first letter of all of the
# inputs and grouping them next to each other. Do this for every letter, see
# example below!
#
# E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"
#
# Note: You can expect all of the inputs to be the same length.


def triple_trouble(one, two, three):
    return "".join(a + b + c for a, b, c in zip(one, two, three))


if __name__ == '__main__':
    print(triple_trouble("Bm", "aa", "tn"))


# Best solutions:


def triple_trouble(one, two, three):
    return ''.join(''.join(a) for a in zip(one, two, three))


def triple_trouble(one, two, three):
    ans = ''
    for i in range(len(one)):
        ans+=one[i]
        ans+=two[i]
        ans+=three[i]
    return ans
