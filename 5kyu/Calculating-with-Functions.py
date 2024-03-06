# This time we want to write calculations using functions and get the results.
# Let's have a look at some examples:
# 
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# 
# Requirements:
# 
#     There must be a function for each number from 0 ("zero") to 9 ("nine")
#     There must be a function for each of the following mathematical
#     operations: plus, minus, times, divided_by
#     Each calculation consist of exactly one operation and two numbers
#     The most outer function represents the left operand, the most inner
#     function represents the right operand
#     Division should be integer division. For example, this should return 2,
#     not 2.666666...:
# 
# eight(divided_by(three()))


def zero(func=None):
    if func is None:
        return 0
    else:
        return func(0)


def one(func=None): return 1 if func is None else func(1)
def two(func=None): return 2 if func is None else func(2)
def three(func=None): return 3 if func is None else func(3)
def four(func=None): return 4 if func is None else func(4)
def five(func=None): return 5 if func is None else func(5)
def six(func=None): return 6 if func is None else func(6)
def seven(func=None): return 7 if func is None else func(7)
def eight(func=None): return 8 if func is None else func(8)
def nine(func=None): return 9 if func is None else func(9)


def plus(y):
    return lambda x: x + y


def minus(y):
    return lambda x: x - y


def times(y):
    return lambda x: x * y


def divided_by(y):
    return lambda x: x // y


print(seven(times(five())))
print(three(times(zero())))

# Best solutions

def identity(a): return a

def zero(f=identity): return f(0)
def one(f=identity): return f(1)
def two(f=identity): return f(2)
def three(f=identity): return f(3)
def four(f=identity): return f(4)
def five(f=identity): return f(5)
def six(f=identity): return f(6)
def seven(f=identity): return f(7)
def eight(f=identity): return f(8)
def nine(f=identity): return f(9)

def plus(b): return lambda a: a + b
def minus(b): return lambda a: a - b
def times(b): return lambda a: a * b
def divided_by(b): return lambda a: a // b


def zero(arg=""):  return eval("0" + arg)
def one(arg=""):   return eval("1" + arg)
def two(arg=""):   return eval("2" + arg)
def three(arg=""): return eval("3" + arg)
def four(arg=""):  return eval("4" + arg)
def five(arg=""):  return eval("5" + arg)
def six(arg=""):   return eval("6" + arg)
def seven(arg=""): return eval("7" + arg)
def eight(arg=""): return eval("8" + arg)
def nine(arg=""):  return eval("9" + arg)

def plus(n):       return '+' + str(n)
def minus(n):      return '-' + str(n)
def times(n):      return '*' + str(n)
def divided_by(n): return '//' + str(n)


id_ = lambda x: x
number = lambda x: lambda f=id_: f(x)
zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))
plus = lambda x: lambda y: y + x
minus = lambda x: lambda y: y - x
times = lambda x: lambda y: y * x
divided_by = lambda x: lambda y: y // x