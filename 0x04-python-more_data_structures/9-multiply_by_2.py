#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None

    new_dictionary = {}

    for elements in a_dictionary.keys():
        new_dictionary[elements] = a_dictionary[elements] * 2

    return new_dictionary
