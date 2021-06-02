#!/usr/bin/python3
'''A function that returns True if the object
is an instance of a class that inherited (directly or indirectly)
from the specified class ; otherwise False. '''


def inherits_from(obj, a_class):
    '''Fetermine if and of is and inhiratnce from a respectve class
    Arg:
        obj: the obj to check:
        a_class: the class to evaluate
    Return: True if it is inharatge and false if is not'''
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True

    else:
        return False
