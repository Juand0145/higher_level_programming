#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None

    new_list = sum(set(my_list))

    return new_list
