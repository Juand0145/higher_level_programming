#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    n_elemets = len(my_list)

    if (idx < 0 or idx > n_elemets - 1):
        return None

    my_list[idx] = element

    return my_list
