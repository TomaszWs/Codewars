# Complete the function which converts a binary number (given as a string) to a
# decimal number.


def bin_to_decimal(inp):
    return int(inp, 2)


if __name__ == '__main__':
    print(bin_to_decimal("10"))


# Best solutions:


def bin_to_decimal(inp):
    num = 0
    inp = inp[::-1]
    for i in range(len(inp)):
        num += int(inp[i]) * 2 ** i
    return num
