# Create a function that returns the CSV representation of a two-dimensional
# numeric array.
#
# Example:
#
# input:
# [[0, 1, 2, 3, 4],
#  [10, 11, 12, 13, 14],
#  [20, 21, 22, 23, 24],
#  [30, 31, 32, 33, 34]]
#
# output:
# '0,1,2,3,4\n'
# +'10,11,12,13,14\n'
# +'20,21,22,23,24\n'
# +'30,31,32,33,34'
#
# Array's length > 2.
#
# More details here:
# https: // en.wikipedia.org / wiki / Comma - separated_values
#
# Note: you shouldn't escape the \n, it should work as a new line.


def to_csv_text(array):
    return "\n".join([",".join(map(str, a)) for a in array])


if __name__ == "__main__":
    print(to_csv_text([
            [0, 1, 2, 3, 45],
            [10, 11, 12, 13, 14],
            [20, 21, 22, 23, 24],
            [30, 31, 32, 33, 34]
        ]))


# Best solutions:


def toCsvText(array) :
   return '\n'.join(','.join(str(n) for n in lst) for lst in array)


def toCsvText(array):
    rs = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = str(array[i][j])
        rs.append(','.join(array[i]))
    return '\n'.join(rs)
