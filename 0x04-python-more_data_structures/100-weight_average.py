#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0

    numerator = sum(map(lambda number: number[0] * number[1], my_list))
    denominator = sum(map(lambda number: number[1], my_list))

    result = numerator / denominator

    return result
