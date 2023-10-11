#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    row_len = len(matrix)
    column = len(matrix[0])
    transposed = []
    for i in range(row_len):
        transposed_row = []
        for j in range(column):
            square = (matrix[i][j])**2
            transposed_row.append(square)
        transposed.append(transposed_row)
    return (transposed)
