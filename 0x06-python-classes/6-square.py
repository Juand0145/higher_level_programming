#!/usr/bin/python3
"""Create a square class"""


class Square:
    """Creating a privates instances atributes: size and position"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    def my_print(self):
        """Print a square of # give it the respective size"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end='')
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)

                print()

    @property
    def position(self):
        """Making public psotion"""
        return self.__position

    @position.setter
    def position(self, value):
        """giving the property setter"""
        if type(value) != tuple or len(value) != 2 or \
                any(map(lambda x: x < 0, value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        if any(map(lambda x: type(x) != int, value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        else:
            self.__position = value
