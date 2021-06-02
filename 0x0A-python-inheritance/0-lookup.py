#!/usr/bin/python3
'''Is a function that returns the list of
available attributes and methods of an object '''


def lookup(obj):
    '''Return the list of atributes in the respective object'''
    return dir(obj)
