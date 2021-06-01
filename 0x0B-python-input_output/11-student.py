#!/usr/bin/python3
'''Class Student that defines a student by:
(based on 10-student.py) '''


class Student:
    '''Creatiing the public atributes'''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrives a dictionary representation of the student instances'''
        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for values in attrs:
                if values in self.__dict__:
                    my_dict.update({values: self.__dict__[values]})

            return my_dict

        return self.__dict__.copy()

    def reload_from_json(self, json):
        '''Replaces all attributes of the Student instance'''
        for x in json:
            self.__dict__.update({x: json[x]})
