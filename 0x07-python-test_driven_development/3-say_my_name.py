#!/usr/bin/python3
'''A function that prints My name is <first name> <last name>'''


def say_my_name(first_name, last_name=""):
    '''The function that print the full name
    first name and last name must be strings'''
    if type(first_name) != str:
        raise TypeError('first_name must be a string')

    if type(last_name) != str:
        raise TypeError('last_name must be a string')

    print("My name is {:s} {:s}".format(first_name, last_name))
