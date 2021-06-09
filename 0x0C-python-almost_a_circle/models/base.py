#!/usr/bin/python3
'''Module base. Definse the characteristic of other classes
    this is gonna be the base to conrtuct the other clasess'''
import json
from os import path
import csv



class Base:
    '''This class will be the “base” of all other classes in this project
    to be create'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Initializing instance: yourself'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries
        an does a lot of thinks'''
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Function that deserializesin CSV,
        save instances to a CSV file"""
        if list_objs is None:
            list_objs = []

        if cls.__name__ == 'Rectangle':
            attrs = ('id', 'width', 'height', 'x', 'y')
        elif cls.__name__ == 'Square':
            attrs = ('id', 'size', 'x', 'y')
        list_objs = ([getattr(o, a) for a in attrs] for o in list_objs)
        with open(cls.__name__ + '.csv', 'wt', newline='') as file:
            writer = csv.writer(file)
            for row in list_objs:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Function that serializes in CSV,
        load from a CSV file"""
        if not path.exists(cls.__name__ + '.csv'):
            return []
        if cls.__name__ == 'Rectangle':
            attrs = ('id', 'width', 'height', 'x', 'y')
        elif cls.__name__ == 'Square':
            attrs = ('id', 'size', 'x', 'y')
        with open(cls.__name__ + '.csv', 'rt', newline='') as my_file:
            reader = csv.reader(my_file)
            my_objects = list(reader)
        my_objects = ((int(i) for i in l) for l in my_objects)
        return [cls.create(**dict(zip(attrs, l))) for l in my_objects]
