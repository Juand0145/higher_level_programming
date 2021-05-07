#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    n_matrix = \
        list(map(lambda x: list(map(lambda value: value ** 2, x)), matrix))

    return n_matrix
