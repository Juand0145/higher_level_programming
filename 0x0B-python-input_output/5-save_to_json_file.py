#!/usr/bin/python3
'''A function that writes an Object to a text file,
using a JSON representation'''
import json


def save_to_json_file(my_obj, filename):
    '''Create a file with json code'''
    with open(filename, mode="w+", encoding="utf-8") as my_file:
        file = my_file.write(json.dumps(my_obj))

    return file
