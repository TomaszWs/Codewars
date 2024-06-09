# Given a logarithm base X and two values A and B, return a sum of logratihms
# with the base X: log⁡XA+log⁡XB \log_XA + \log_XB logX​A+logX​B.


from math import log


def logs(x, a, b):
    return log(a, x) + log(b, x)


if __name__ == "__main__":
    print(logs(10, 2, 3))


# Best solutions:

