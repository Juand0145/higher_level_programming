#!/usr/bin/python3
'''a function that returns True if the object is
an instance of, or if the object is aninstance of a class
that inherited from, the specified class ; otherwise False.'''


def is_kind_of_class(obj, a_class):
    '''Look if is and instance or inherited from a_class
    Args:
        obj:The object to check
        a_class: tha class to verify
    Return: true if is the same clase or heritage or false if is not'''
    if isinstance(obj, a_class):
        return True
    else:
        return False
