#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return None

    for keys in sorted(a_dictionary):
        print("{:s}: {}".format(keys, a_dictionary[keys]))
