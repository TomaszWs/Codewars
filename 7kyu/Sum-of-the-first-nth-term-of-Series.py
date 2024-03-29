# Task:
#
# Your task is to write a function which returns the sum of following series
# upto nth term(parameter).
#
# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
#
# Rules:
#
#     You need to round the answer to 2 decimal places and return it as String.
#
#     If the given value is 0 then it should return 0.00
#
#     You will only be given Natural Numbers as arguments.
#
# Examples:(Input --> Output)
#
# 1 --> 1 --> "1.00"
# 2 --> 1 + 1/4 --> "1.25"
# 5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
#


def series_sum(n):
    x = 1
    m = []
    while n > 0 :
        m.append(1/x)
        x +=3
        n -= 1
    return str('%.2f' %sum(m))

n = 0
print(series_sum(n))


# Best solutions:


def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))


def series_sum(n):
    sum = 0.0
    for i in range(0,n):
        sum += 1 / (1 + 3 * float(i))
    return '%.2f' % sum