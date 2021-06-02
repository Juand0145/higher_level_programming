#!/usr/bin/python3
'''A function that returns True if the object is exactly
an instance of the specified class ; otherwise False. '''


def is_same_class(obj, a_class):
    '''Detemine if and object is and instance of given a_class
    Args:
        obj: The object to find the class
        a_class: the class to verify

    Return: True if is the same Class or false if is not'''
    if type(obj) != a_class:
        return False
    else:
        return True
