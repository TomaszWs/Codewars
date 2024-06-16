# Gobang Weight Table
#
# You will generate a weight table of gobang game in less than 100 characters.
# The outermost layer of the table is 0, and the number is incremented by one
# for each layer inside.
#
# Your task is to define a function, which returns weight table in different
# izes(N) as the examples below.
# Examples:
# Input: 3
# Output:
#
# [[0, 0, 0],
#  [0, 1, 0],
#  [0, 0, 0]]
#
# Input: 5
# Output:
#
# [[0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 0],
#  [0, 1, 2, 1, 0],
#  [0, 1, 1, 1, 0],
#  [0, 0, 0, 0, 0]]
#
# Input: 9
# Output:
#
# [[0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 1, 1, 1, 1, 0],
#  [0, 1, 2, 2, 2, 2, 2, 1, 0],
#  [0, 1, 2, 3, 3, 3, 2, 1, 0],
#  [0, 1, 2, 3, 4, 3, 2, 1, 0],
#  [0, 1, 2, 3, 3, 3, 2, 1, 0],
#  [0, 1, 2, 2, 2, 2, 2, 1, 0],
#  [0, 1, 1, 1, 1, 1, 1, 1, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0]]
#
# Notes
#
#     3 <= N <= 99, N will ONLY be odd number.
#     Your code cannot be longer than 100 characters.


def weight_table(n):
    return [[min(row, col, n-1-row, n-1-col) for col in range(n)] for row
            in range(n)]


if __name__ == "__main__":
    print(weight_table(3))


# Best solutions:


def weight_table(n):
    return [[min(i, j, n-i-1, n-j-1) for i in range(n)] for j in range(n)]


weight_table=lambda n:[[min(i,j,n+~i,n+~j)for j in range(n)]for i in range(n)]
