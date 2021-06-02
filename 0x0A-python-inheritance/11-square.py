#!/usr/bin/python3
'''A class Square that inherits from Rectangle (9-rectangle.py)'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A class call square'''

    def __init__(self, size):
        '''Defining the square atributes'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Calculating the area'''
        area = self.__size ** 2
        return area

    def __str__(self):
        '''Allow to prith the aprameters of the square'''
        return ("[Square] {}/{}".format(self.__size, self.__size))
