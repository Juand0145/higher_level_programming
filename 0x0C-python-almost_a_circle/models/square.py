#!/usr/bin/python3
'''A sub class Square based on rectangle'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''A sub class Square based on rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initializing the square'''
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        '''Getter the atribute size'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setting the atribute size using the width atribute to
        define the size'''
        self.width = value
        self.height = value

    def __str__(self):
        '''Adding and specifis str to the square'''
        s = "[Square] ({}) {}/{} - {}".format(self.id,
                                              self.x, self.y, self.width)
        return s

    def update(self, *args, **kwargs):
        '''Update the atrbutes in the instance square
        im just putting some words to confirm the check is running'''
        atributes = ["id", "size", "x", "y"]
        dic = zip(atributes, args)

        for atribute_name, value in dic:
            if atribute_name == "size":
                self.size = value
            if atribute_name == "x":
                self.x = value
            if atribute_name == "y":
                self.y = value
            if atribute_name == "id":
                self.id = value

        if kwargs is not None:
            for atribute_name, value in kwargs.items():
                if atribute_name == "size":
                    self.size = value
                if atribute_name == "x":
                    self.x = value
                if atribute_name == "y":
                    self.y = value
                if atribute_name == "id":
                    self.id = value

    def to_dictionary(self):
        '''Return the dictionary that represent the square'''
        atributes = ["id", "size", "x", "y"]
        return {key: getattr(self, key) for key in atributes}
