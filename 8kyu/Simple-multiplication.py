# This kata is about multiplying a given number by eight if it is an even
# number and by nine otherwise.


def simple_multiplication(number):
    return number*8 if number%2 == 0 else number*9


print(simple_multiplication(2))
print(simple_multiplication(1))
print(simple_multiplication(8))
print(simple_multiplication(4))
print(simple_multiplication(5))


# Best solutions:


def simple_multiplication(number) :
    return number * 9 if number % 2 else number * 8


def simple_multiplication(n) :
    return n * (8 + n%2)


def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    return number*9
