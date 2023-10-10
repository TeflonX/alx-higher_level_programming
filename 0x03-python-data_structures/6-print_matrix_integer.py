#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    column = len(matrix[0])
    row = len(matrix)
    for i in range(row):
        for j in range(column):
            print('{:d}'.format(matrix[i][j]), end='')
            if j != column - 1:
                print(' ', end='')
        if i != (row - 1):
            print()
    print()
