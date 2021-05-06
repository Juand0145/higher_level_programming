#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    n_elements = len(my_list) - 1

    if idx < 0 or idx > n_elements:
        return my_list

    del(my_list[idx])

    return(my_list)
