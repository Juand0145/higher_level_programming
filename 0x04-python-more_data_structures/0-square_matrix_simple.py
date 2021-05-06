#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None

    new_matrix = [[j**2 for j in i] for i in matrix]

    return new_matrix
