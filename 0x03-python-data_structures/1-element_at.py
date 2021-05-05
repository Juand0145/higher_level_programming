#!/usr/bin/python3
def element_at(my_list, idx):
    n_elemets = len(my_list)

    if (idx < 0 or idx > n_elemets):
        return None

    return my_list[idx]
