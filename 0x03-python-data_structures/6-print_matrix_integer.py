#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for col in i[:-1]:
            print("{:d}".format(col), end=" ")

        if i:
            print("{:d}".format(i[-1]))

        else:
            print()
