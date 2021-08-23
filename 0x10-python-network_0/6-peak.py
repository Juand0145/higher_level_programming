#!/usr/bin/python3
"""File that contain the function find_peak"""


def find_peak(list):
    """Function that find the biggest element in a list"""
    if list is None or list == []:
        return None

    lo = 0
    hi = len(list)
    mid = ((hi - lo) // 2) + lo
    mid = int(mid)

    if hi == 1:
        return list[0]

    if hi == 2:
        return max(list)

    if list[mid] >= list[mid - 1] and\
            list[mid] >= list[mid + 1]:
        return list[mid]

    if mid > 0 and list[mid] < list[mid + 1]:
        return find_peak(list[mid:])

    if mid > 0 and list[mid] < list[mid - 1]:
        return find_peak(list[:mid])