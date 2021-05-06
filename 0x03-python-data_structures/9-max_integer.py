#!/usr/bin/python3
def max_integer(my_list=[]):
    max_number = 0

    if  not my_list:
        return None

    for number in my_list:
        if number > max_number:
            max_number = number

    return (max_number)
