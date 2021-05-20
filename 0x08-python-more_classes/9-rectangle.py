#!/usr/bin/python3
'''Creatiing a class call rectangle'''


class Rectangle:
    '''Defining the class'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Defining the class'''
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
                print_rectangle += '{}'.format(self.print_symbol)
            print_rectangle += '\n'
        return print_rectangle[:-1]

    def __repr__(self):
        '''creating a method the dimentions of the rectngle'''
        dime = "Rectangle({}, {})".format(self.__width, self.__height)
        return dime

    def __del__(self):
        '''A method that deletes and instance and print a message'''
        print("Bye rectangle...")
        Rectangle.number_of_instances += -1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''And static method that return the bigest rectangle'''
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''Creating a square using the rectangle'''
        square = cls(size, size)
        return square
