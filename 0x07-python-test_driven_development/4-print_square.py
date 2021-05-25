#!/usr/bin/python3
'''A function that prints a square with the character # '''


def print_square(size):
    '''A function that print asaqure with the simbol #
    we must ensure that size must be and integer and be a value
    above of 0'''

    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(round(size)):
        print("#" * round(size))
