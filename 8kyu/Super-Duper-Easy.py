# Make a function that returns the value multiplied by 50 and increased by 6.
# If the value entered is a string it should return "Error".


def problem(a):
    return (a * 50) + 6 if type(a) != str else "Error"


if __name__ == '__main__':
    print(problem(1))


# Best soutions:


def problem(a):
    try:
        return a * 50 + 6
    except TypeError:
        return "Error"


def problem(a):
    return "Error" if isinstance(a,str) else a*50+6


def problem(a):
    return "Error" if a == str(a) else a * 50 + 6
