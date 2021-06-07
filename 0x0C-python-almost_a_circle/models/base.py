#!/usr/bin/python3
import json
'''Module base.
Definse the characteristic of other classes'''


class Base:
    '''This class will be the “base” of all other classes in this project'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initializing instance:
        Arg:
            id = the id of the respective instace'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Method that writes the JSON string representation
        of list_objs to a file
        Arguments:
            cls, its a representation of the class
            list_objs = s a list of instances who inherits of Base'''
        if not list_objs:
            list_objs = []

        with open("{}.json".format(cls.__name__), 'w') as my_file:
            my_file.write(cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        '''Returns the list of the JSON string representation json_string
        Arguments:
            json_string:  is a string representing a list of dictionaries'''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''that returns an instance with all attributes already set
        Arguments:
            dictionary: '''
        if cls.__name__ == "Rectangle":
            canvas = cls(1, 1)
        elif cls.__name__ == "Square":
            canvas = cls(1)
        canvas.update(**dictionary)
        return canvas

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances:'''
        try:
            with open("{}.json".format(cls.__name__), 'r') as jf:
                dictionaries = cls.from_json_string(jf.read())
                return [cls.create(**d) for d in dictionaries]

        except FileNotFoundError:
            return []
