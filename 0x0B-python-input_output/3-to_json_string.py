#!/usr/bin/python3
'''A function that returns the JSON representation of an object (string): '''
import json


def to_json_string(my_obj):
    '''Printing the Json file'''
    file = json.dumps(my_obj)

    return file
