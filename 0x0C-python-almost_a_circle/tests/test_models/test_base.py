#!/usr/bin/python3
"""Contains tests for Base class"""

import unittest
import inspect
import pep8
import json
from models import base
Base = base.Base


class TestBaseDocs(unittest.TestCase):
    """Allow Tests to check the documentation and style of Base class"""
    @classmethod
    def setUpClass(cls):
        """Allow Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_pep8(self):
        """Allow Test that models/base.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring(self):
        """Allow Tests for the module docstring"""
        self.assertTrue(len(base.__doc__) >= 1)

    def test_classdocstring(self):
        """Allow Tests for the Base class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_funcdocstrings(self):
        """Allow Tests for the presence of docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestBase(unittest.TestCase):
    """Allow Tests to check functionality of Base class"""
    def test_manyargs(self):
        """test too many args to init"""
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def test_id_set_clas(self):
        """Tests id as not None"""
        b98 = Base(98)
        self.assertEqual(b98.id, 98)

    def test_private(self):
        """Tests nb_objects as a private instance attribute"""
        b = Base(3)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_jsonstring(self):
        """Allow Tests regular to json string"""
        Base._Base__nb_objects = 0
        d1 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        d2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_s = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_s) is str)
        d = json.loads(json_s)
        self.assertEqual(d, [d1, d2])

    def test_emptyjson_string(self):
        """Allow Test for passing empty list/ None"""
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_Nonejson_String(self):
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_jsonstring(self):
        """Allow Tests regular from_json_string"""
        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
{"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})

    def test_fjsempty(self):
        """Allow Tests from_json_string with an empty string"""
        self.assertEqual([], Base.from_json_string(""))

    def test_fjsNone(self):
        """Allow Tests from_json_string with an empty string"""
        self.assertEqual([], Base.from_json_string(None))
