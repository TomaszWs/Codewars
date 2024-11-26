# Your goal is to return multiplication table for number that is always an
# integer from 1 to 10.
#
# For example, a multiplication table (string) for number == 5 looks like
# below:
#
# 1 * 5 = 5
# 2 * 5 = 10
# 3 * 5 = 15
# 4 * 5 = 20
# 5 * 5 = 25
# 6 * 5 = 30
# 7 * 5 = 35
# 8 * 5 = 40
# 9 * 5 = 45
# 10 * 5 = 50
#
# P. S. You can use \n in string to jump to the next line.
#
# Note: newlines should be added between rows, but there should be no trailing
# newline at the end. If you're unsure about the format, look at the sample
# tests.


def multi_table(number):
    return (f"1 * {number} = {number}\n2 * {number} = {number*2}\n3 * "
            f"{number} = {number*3}\n4 * {number} = {number*4}\n5 * "
            f"{number} = {number*5}\n6 * {number} = {number*6}\n7 * "
            f"{number} = {number*7}\n8 * {number} = {number*8}\n9 * "
            f"{number} = {number*9}\n10 * {number} = {number*10}")


if __name__ == '__main__':
    print(multi_table(5))


# Best solutions:


def multi_table(number):
    return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))


def multi_table(number):
    table = ["{0} * {1} = {2}".format(i, number, i * number) for i in range(1, 11)]
    return '\n'.join(table)