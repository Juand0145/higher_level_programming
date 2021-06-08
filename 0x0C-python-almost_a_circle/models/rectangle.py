#!/usr/bin/python3
'''Module Rectangle'''
from models.base import Base


class Rectangle(Base):
    '''Class that represent a rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializing Rectangle:
        Arguments:
            width, hegight = dimensions of he rectangle
            x, y = The position of the rectangle'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''width atribute'''
        return self.__width

    @width.setter
    def width(self, width):
        '''Asigning atribute width'''
        if type(width) != int:
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        '''height atribute'''
        return self.__height

    @height.setter
    def height(self, height):
        '''Asigning atribute height'''
        if type(height) != int:
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        '''x atribute'''
        return self.__x

    @x.setter
    def x(self, x):
        '''Asigning atribute x'''
        if type(x) != int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        '''y atribute'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Asigning atribute x'''
        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        '''Public instance Method that evaluate the area of the rectangle'''
        area = self.__height * self.__width
        return area

    def display(self):
        '''Public instance Method that print and rectangle with #'''
        if self.__height == 0 or self.__width == 0:
            print('')

        else:
            if self.__y > 0:
                print((self.__y - 1) * '\n')
            for i in range(self.__height):
                print(self.__x * ' ' + self.__width * '#')

    def __str__(self):
        '''Create a string that defines the rectangle'''
        data = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height)

        return data

    def update(self, *args, **kwargs):
        '''Update the atributes in the current instance
        Arguments:
            *args: argument to update'''
        atributes = ["id", "width", "height", "x", "y"]
        dic = zip(atributes, args)

        for atribute_name, value in dic:
            if atribute_name == "width":
                self.__width = value
            if atribute_name == "height":
                self.__height = value
            if atribute_name == "x":
                self.__x = value
            if atribute_name == "y":
                self.__y = value
            if atribute_name == "id":
                self.id = value

        if kwargs is not None:
            for atribute_name, value in kwargs.items():
                if atribute_name == "width":
                    self.__width = value
                if atribute_name == "height":
                    self.__height = value
                if atribute_name == "x":
                    self.__x = value
                if atribute_name == "y":
                    self.__y = value
                if atribute_name == "id":
                    self.id = value

    def to_dictionary(self):
        '''Return teh dictionary taht represent the rectangle'''
        atributes = ["id", "width", "height", "x", "y"]
        return {key: getattr(self, key) for key in atributes}
