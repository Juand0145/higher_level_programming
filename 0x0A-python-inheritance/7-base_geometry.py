#!/usr/bin/python3
'''A class call BaseGeometry'''


class BaseGeometry:
    ''''Empty class'''
    def area(self):
        '''And empty method call area'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Method that validates value'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))
