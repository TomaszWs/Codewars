# Task
#
# Find all the saddle points of a non-empty matrix of integers. A
# saddle point is an element that is minimal in its row and maximal in
# its column. Return them in a list of (row,column) coordinates. The
# order of the saddle points in the list is irrevelant.
# Example
#
# Consider the following matrix:
#
# 6 4 3
# 7 0 2
# 4 3 2
# 5 3 3
#
#     The row minimums are 3, 0, 2, 3 (at positions 1 and 2).
#     The column maximums are 7, 4, 3 (at positions 0 and 3).
#     Therefore the 3's in the 3rd column are saddle points, but the
#     3's in the 2nd column are not.
#     Return [(0,2), (3,2)]] or [(3,2), (0,2)].
#
# Constraints
#
# Number of rows r and number of columns c satisfy1 ≤ r,c ≤ 500. So
# you should think about efficiency (a little).
# Note
#
# Matrix saddle points are used in game theory to identify optimal
# strategies in two-person zero-sum games - see here. There is a
# related saddle point concept for functions, which has even wider
# applications - see here.


def find_saddle_points(matrix):
    r = len(matrix)
    c = len(matrix[0])
    row_min = [min(row) for row in matrix]
    col_max = [max(matrix[i][j] for i in range(r)) for j in range(c)]
    result = []
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == row_min[i] and matrix[i][j] == col_max[j]:
                result.append((i, j))
    return result


if __name__ == '__main__':
    print(find_saddle_points([[3, 1, 3], [3, 2, 4], [0, 1, 5]]))


# Best solutions:


def find_saddle_points(matrix):
    columns = list(zip(*matrix))
    min_row = list(map(min, matrix))
    max_col = list(map(max, columns))

    return [(row, col)
            for row in range(len(matrix))
            for col in range(len(columns))
            if min_row[row] == max_col[col]
            ]

def find_saddle_points(m):
    r=len(m);c=len(m[0]);mn=[min(x) for x in m];mx=[max(m[i][j] for i in range(r))for j in range(c)]
    return [(i,j)for i in range(r)for j in range(c)if m[i][j]==mn[i]and m[i][j]==mx[j]]


import numpy as np


def find_saddle_points(matrix: list[list]) -> list[tuple]:
    matrix_array = np.asarray(matrix)

    row_min = matrix_array.min(axis=1, keepdims=True)
    col_max = matrix_array.max(axis=0, keepdims=True)

    mask = (matrix_array == row_min) & (matrix_array == col_max)

    return [tuple(idx) for idx in np.argwhere(mask)]
