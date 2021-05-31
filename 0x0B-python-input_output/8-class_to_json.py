#!/usr/bin/python3
'''A function that returns the dictionary
description with simple data structure  '''


def class_to_json(obj):
    '''Return the obj atribute as a dictionary'''
    return obj.__dict__