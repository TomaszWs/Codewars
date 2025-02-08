# Complete the function which converts hex number (given as a string) to a
# decimal number.


def hex_to_dec(s):
    return int(s, 16)


if __name__ == '__main__':
    print(hex_to_dec("a"))


# Best solutions:


def hex_to_dec(s):
    key = "0123456789abcdef"
    n = 0
    res = 0
    for l in s[::-1]:
        res += key.index(l) * (16. ** n)
        n += 1

    return int(res)
