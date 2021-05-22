#!/usr/bin/python3
'''A lass or object attribute, that prevents the user from
dynamically creating new instance attributes, except if the
new instance attribute is called first_name.'''


class LockedClass:
    '''__slots__: List of strings which may serve as valid attribute
    identifiers as in `self.__dict__`.'''
    __slots__ = ['first_name']
