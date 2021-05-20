#!/usr/bin/python3
'''Creatiing a class call rectangle'''


class Rectangle:
    '''Defining the class'''

    def __init__(self, width=0, height=0):
        '''Defining the class'''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''defining width property to retrive it'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set the widh property'''
        if type(value) != int or value < 0:
            raise TypeError("width must be an integer")
        else:
            self.__width = value

    @property
    def height(self):
        '''defining height property to retrive it'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set the height property'''
        if type(value) != int or value < 0:
            raise TypeError("height must be >= 0")
        else:
            self.__height = value
