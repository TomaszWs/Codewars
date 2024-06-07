# Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.
# Examples (input -> output)
#
# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"


def repeat_str(repeat, string):
    return repeat*string


if __name__ == "__main__":
    print(repeat_str(6, "I"))


# Best solutions:


def repeat_str(repeat, string):
    solution = ""
    for i in range(repeat):
        solution += string
    return solution
