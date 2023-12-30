# Complete the solution so that it returns true if the first argument(string)
# passed in ends with the 2nd argument (also a string).
#
# Examples:
#
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false


def solution(text, ending):
    return text.endswith(ending)


text = "abc"
ending = "bc"
print(solution(text, ending))

# Best solutions:


solution = str.endswith


def solution(string, ending):
    return ending in string[-len(ending):]