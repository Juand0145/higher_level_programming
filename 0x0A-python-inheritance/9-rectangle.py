#!/usr/bin/python3
'''A class Rectangle that inherits from BaseGeometry (7-base_geometry.py) '''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A class that represent a rectangle'''
    def __init__(self, width, height):
        '''A class to define a rectangle
        Arg:
         width
         height'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''A method that calculate the area'''
        area = self.__height * self.__width
        return area

    def __str__(self):
        ''' The str function that allow to print'''
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
