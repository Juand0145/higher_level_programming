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

    def area(self):
        '''Creating a public instance method tha calculates the area'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''creating a public instance method that calculates the perimeter'''
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        '''creating a method that print a rectangle of #'''
        if self.__height == 0 or self.__width == 0:
            return ""
        print_rectangle = ''
        for i in range(self.__height):
            for j in range(self.__width):
                print_rectangle += '#'
            print_rectangle += '\n'
        return print_rectangle[:-1]

    def __repr__(self):
        '''creating a method the dimentions of the rectngle'''
        dime = "Rectangle({}, {})".format(self.__width, self.__height)
        return dime
