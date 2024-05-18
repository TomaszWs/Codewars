# Jack really likes his number five: the trick here is that you have to
# multiply each number by 5 raised to the number of digits of each numbers,
# so, for example:
#
#   3 -->    15  (  3 * 5¹)
#  10 -->   250  ( 10 * 5²)
# 200 --> 25000  (200 * 5³)
#   0 -->     0  (  0 * 5¹)
#  -3 -->   -15  ( -3 * 5¹)


def multiply(n):
    return n * (5 ** len(str(abs(n))))


if __name__ == "__main__":
    print(multiply(-3))


# Best solutions:


def multiply(n):
    return n * 5 ** int_len(n)


def int_len(n):
    n = abs(n)
    length = 0
    while n:
        length += 1
        n //= 10
    return length


def multiply(n):
    s = str(n)
    s = s.replace('-', '')
    a = len(s)

    return n * 5 ** a
