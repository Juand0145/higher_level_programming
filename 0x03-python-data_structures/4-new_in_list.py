#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    n_lists = [i for i in my_list]
    if idx < 0 or idx > len(n_lists) - 1:
        return n_lists
    n_lists[idx] = element
    return n_lists
