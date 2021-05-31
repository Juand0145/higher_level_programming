#!/usr/bin/python3
'''A function that creates an Object from a “JSON file” '''
import json


def load_from_json_file(filename):
    '''Return and object acoreding to the json fil '''
    with open(filename, mode="r") as my_file:
        object = json.load(my_file)

    return object
