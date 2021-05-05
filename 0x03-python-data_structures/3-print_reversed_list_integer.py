#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = -1
    counter = -len(my_list)

    while (i >= counter):
        print("{:d}".format(my_list[i]))
        i -= 1
