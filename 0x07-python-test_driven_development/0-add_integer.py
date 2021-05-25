#!/usr/bin/python3
'''A function that adds 2 integers.
if they are float it converts into integers'''


def add_integer(a, b=98):
    '''Return the addintion of a and b'''

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
