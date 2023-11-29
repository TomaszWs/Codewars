# Write Number in Expanded Form
#
# You will be given a number and you will need to return it as a string in
# Expanded Form. For example:
#
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
#
# NOTE: All numbers will be whole numbers greater than 0.
#
# If you liked this kata, check out part 2!!


def expanded_form(num):
    num_string = str(num)
    result = []
    for i, digit in enumerate(num_string):
        if digit != '0':
            result.append(digit + '0' * (len(num_string) - i - 1))
    return ' + '.join(result)


num = 70304
print(expanded_form(num))

# Best solutions:


def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')