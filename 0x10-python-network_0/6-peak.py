#!/usr/bin/python3
"""File that contain the function find_peak"""


def find_peak(list):
    """Function that find the biggest element in a list"""
    if len(list) == 0 or list is None:
        return None

    biggest_number = list[0]

    for number in list:
        if number > biggest_number:
            biggest_number = number

    return biggest_number
