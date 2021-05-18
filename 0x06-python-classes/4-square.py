#!/usr/bin/python3
"""Create a square class"""


class Square:
    """Creating a private instance atribute: size"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

    def area(self):
        """A new Method call: area= size ^ 2"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Making public size"""
        return self.__size

    @size.setter
    def size(self, value):
        """giving the property setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value
