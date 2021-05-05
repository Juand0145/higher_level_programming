#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    array = []
    a = iter(tuple_a)
    b = iter(tuple_b)

    for i in range(2):
        array.append(next(a, 0) + next(b, 0))

    return tuple(array)
