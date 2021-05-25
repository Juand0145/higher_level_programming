#!/usr/bin/python3
'''Is a function that divides all elements of a matrix.'''


def matrix_divided(matrix, div):
    '''Divided all element of the amtrix by the number div
    matrix must be a matrix (list of lists) of integers/floats
    Each row of the matrix must have the same size
    and obviusly cant be dived by 0'''

    if type(matrix) != list or len(matrix) == 0 or not matrix:
        raise TypeError("matrix must be a matrix" +
                        " (list of lists) of integers/floats")

    n_elements_in_row = []

    for row in matrix:
        try:
            n_elements_in_row.append(len(row))

        except:
            raise TypeError("matrix must be a matrix" +
                            " (list of lists) of integers/floats")

        if len(row) == 0:
            raise TypeError("matrix must be a matrix" +
                            " (list of lists) of integers/floats")

        for number in row:
            if type(number) not in [int, float]:
                raise TypeError("matrix must be a matrix" +
                                " (list of lists) of integers/floats")

    if not all(x == n_elements_in_row[0] for x in n_elements_in_row):
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    new_matrix = list(map(lambda x:
                          list(map(lambda y:
                                   round(y / div, 2), x)), matrix))

    return new_matrix
