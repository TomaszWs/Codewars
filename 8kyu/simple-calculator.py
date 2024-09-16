# You are required to create a simple calculator that returns the result of
# addition, subtraction, multiplication or division of two numbers.
#
# Your function will accept three arguments:
# The first and second argument should be numbers.
# The third argument should represent a sign indicating the operation to
# perform on these two numbers.
#
# if the variables are not numbers or the sign does not belong to the list
# above a message "unknown value" must be returned.
# Example:
#
# calculator(1, 2, '+') => 3
# calculator(1, 2, '$') # result will be "unknown value"
#
# Good luck!


def calculator(x,y,op):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return "unknown value"
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y if y != 0 else "unknown value"
    else:
        return "unknown value"


if __name__ == '__main__':
    print(calculator(1, 2, '+'))


# Best solutions:


def calculator(x, y, op):
  return eval(f'{x}{op}{y}') if type(x) == type(y) == int and str(op) in '+-*/' else 'unknown value'


def calculator(x,y,op):
    try:
        assert op in "+-*/"
        return eval('%d%s%d' % (x, op, y))
    except:
        return "unknown value"


def calculator(x, y, op):
    try:
        return {'+': x + y, '-': x - y, '*': x * y, '/': x / y}[op]
    except (TypeError, KeyError):
        return 'unknown value'
