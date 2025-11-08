# This kata revives and extends Calculate the required interest rate,
# which was abandoned years ago in beta.
#
# You have an amount of money initial and want to grow it to amount
# target in n years. Calculate the annual interest rate needed if
# interest is compounded period times each year.
#
# n and period are positive integers. initial and target are real
# numbers, with 0 < initial ≤ target. They are passed into the
# function as decimals, objects of type Decimal. The function should
# return a decimal representing the interest rate as a percentage.
#
# Decimal is a Python class that provides exact representation of
# decimal values. Using the data-type float results in numerical
# inaccuracies because many numbers cannot be exactly represented in
# binary. For example, 0.1 + 0.1 + 0.1 is typically
# 0.30000000000000004 rather than 0.3. Using decimals avoids these
# errors; Decimal('0.1 + 0.1 + 0.1') is exactly equal to
# Decimal('0.3'). Using decimals does not eliminate all numerical
# error; for example, the fact that irrational numbers cannot be
# perfectly represented as fractions is an unavoidable source of
# numerical error. But decimals should be preferred to floats in
# domains, like finance, that require very accurate calculations.
#
# Example 1: Suppose initial = 1000, target = 1210, n = 2 and
# period = 1 (interest compounded annually). The function is called
# with initial = Decimal('1000'), target = Decimal('1210'). It should
# return Decimal('10'), because the needed interest rate is 10%.
# In year 1 you earn 10% * 1000 = 100. This is added to your
# investment at the end of the year, so you have 1100 at the beginning
# of year 2. In year 2 you earn 10% * 1100 = 110. This is added to the
# 1100 at the end of the year, yielding 1210 as desired.
#
# Example 2: To see the effect of the compounding period, change
# period to 2, interest compounded every 6 months. This lowers the
# needed interest rate to approximately 9.762%. In the first 6 months
# you earn (9.762%/2) * 1000 = 48.81. This is added to the 1000.
# In the next 6 months you earn (9.762%/2) * 1048.81 = 51.19.
# This raises the amount to 1048.81 + 51.19 = 1100. You have the same
# amount at the end of year 1 as Example 1, because the lower interest
# rate is compounded more often. Year 2 grows 1100 to 1210 in a
# similar way.
#
# The function should not round the result. If it is used in a wider
# context (e.g. to compare with another investment), we want maximum
# accuracy in the result. We can round the result whenever we want to
# display it. For example 2, the function should return
# Decimal('9.761769634030309398290702800') or something very close to
# it. Answers are accepted if within 0.00000000001 of the solution.
#
# Note: The arithmetic operators + - * / ** (exponentiation) return a
# decimal if both operands are decimals or one is a decimal and the
# other an integer. But they cannot be used if one operand is a
# decimal and the other is a float; the float should first be
# converted to a decimal.
#
# Although not needed for this kata, more information about Decimal is
# here.
#
# Related kata: Simple Interest and Compound Interest


from decimal import Decimal


def required_interest_rate(initial, target, years, period):
    """
    initial: starting amount (decimal)
    target: desired amount (decimal, >= initial)
    years: number of years (positive integer)
    period: number of times interest is compounded per year (positive integer)
    Returns: required annual interest rate as percentage (decimal)
    """
    return ((target / initial) ** (Decimal(1) / (period * years)) - 1) * period * 100


if __name__ == '__main__':
    print(required_interest_rate(Decimal('1000'), Decimal('1210'), 2, 1))


# Best solutions:


from decimal import Decimal

def required_interest_rate(initial, target, n, period):
    total_periods = n * period
    base = target / initial
    factor = base ** (Decimal('1') / total_periods)
    rate = period * (factor - 1)
    return rate * 100
