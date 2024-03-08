# Some numbers have funny properties. For example:
#
#     89 --> 8¹ + 9² = 89 * 1
#     695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
#     46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
#
# Given two positive integers n and p, we want to find a positive integer k,
# if it exists, such that the sum of the digits of n raised to consecutive
# powers starting from p is equal to k * n.
#
# In other words, writing the consecutive digits of n as a, b, c, d ..., is
# there an integer k such that :
# (ap+bp+1+cp+2+dp+3+...)=n∗k(a^p + b^{p + 1} + c^{p + 2} + d^{p + 3} + ...) = n * k(ap+bp+1+cp+2+dp+3+...)=n∗k
#
# If it is the case we will return k, if not return -1.
#
# Note: n and p will always be strictly positive integers.
# Examples:
#
# n = 89; p = 1 ---> 1 since 8¹ + 9² = 89 = 89 * 1
#
# n = 92; p = 1 ---> -1 since there is no k such that 9¹ + 2² equals 92 * k
#
# n = 695; p = 2 ---> 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
#
# n = 46288; p = 3 ---> 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51


def dig_pow(n, p):
    n_string = str(n)
    total_sum = 0
    for i, digit in enumerate(n_string):
        total_sum += int(digit) ** (p + i)
    if total_sum % n == 0:
        return total_sum // n
    else:
        return -1


print(dig_pow(89, 1))


# Best solutions:


def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1


def dig_pow(n, p):
    sum = 0
    for c in str(n):
        sum += int(c) ** p
        p += 1
    if sum % n == 0:
        return sum / n
    else:
        return -1


def dig_pow(n, p):
    k, fail = divmod(sum(int(d)**(p + i) for i, d in enumerate(str(n))), n)
    return -1 if fail else k
