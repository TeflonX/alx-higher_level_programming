#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    a function that returns a matrix with all its elements divided by a given
    number

    Attr:
        matrix: matrix to be divided
        div: divisor

    Return:
        new_matrix: a new matrix
    """
    new_matrix = []
    for x in range(len(matrix)):
        app_list = []
        for y in range(len(matrix[x])):
            if not type(matrix[x][y]) is int and not type(matrix[x][y]) is float:
                raise TypeError('matrix must be a matrix (list of lists) \
                                 of integers/floats')
            if len(matrix[x]) != len(matrix[x+1]):
                raise TypeError('Each row of the matrix must have the \
                    same size')
            app_list.append(round(matrix[x][y]/div, 2))
        new_matrix.append(app_list)

    return new_matrix
