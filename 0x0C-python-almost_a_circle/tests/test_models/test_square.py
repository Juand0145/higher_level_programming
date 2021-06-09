#!/usr/bin/python3
"""Unit tests for Square class"""
import unittest
import sys
import os
import json
from io import StringIO
from models.square import Square
from models.square import __doc__ as module_doc
from models.base import Base


class TestSquare(unittest.TestCase):
    """Square is a subclase form Rectangle and Base"""
    def setUp(self):
        """Redirect stdout to readable buffer to check output of"""
        sys.stdout = StringIO()

    def tearDown(self):
        """Following test completion reassign true stdout file stream to"""
        sys.stdout = sys.__stdout__

    def test_docstrings_square(self):
        """Test for existence of docstrings and all documetation"""
        self.assertIsNotNone(module_doc)
        self.assertIsNotNone(Square.__doc__)
        self.assertIs(hasattr(Square, "__init__"), True)
        self.assertIsNotNone(Square.__init__.__doc__)
        self.assertIs(hasattr(Square, "size"), True)
        self.assertIsNotNone(Square.size.__doc__)
        self.assertIs(hasattr(Square, "__str__"), True)
        self.assertIsNotNone(Square.__str__.__doc__)
        self.assertIs(hasattr(Square, "update"), True)
        self.assertIsNotNone(Square.update.__doc__)
        self.assertIs(hasattr(Square, "to_dictionary"), True)
        self.assertIsNotNone(Square.to_dictionary.__doc__)

    def test_normal(self):
        """Allow that normal uses doent raise any error"""
        s1 = Square(1)
        s2 = Square(1, 2)
        s3 = Square(1, 2, 3)
        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s4.id, 4)

    def test_cnt(self):
        """Test correct number and type of arguments"""
        Base._Base__nb_object = 0
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square(x=1, y=1)

    def test_area_square(self):
        """Test that area method returns correct values"""
        Base._Base__nb_object = 0
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        s4 = Square(99999999999)
        self.assertEqual(s1.area(), 25)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 9)
        self.assertEqual(s4.area(), 99999999999 ** 2)

    def test_display_offset(self):
        """Test that the `display()` method prints correct
        output and creating really good stuf"""
        Base._Base__nb_object = 0
        s1 = Square(5)
        s1_out = "#####\n" \
                 "#####\n" \
                 "#####\n" \
                 "#####\n" \
                 "#####\n"

        s2 = Square(2, 2)
        s2_out = "  ##\n" \
                 "  ##\n"

        s3 = Square(3, 1, 3)
        s3_out = "\n\n\n" \
                 " ###\n" \
                 " ###\n" \
                 " ###\n"

        try:
            s1.display()
            self.assertEqual(sys.stdout.getvalue(), s1_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            s2.display()
            self.assertEqual(sys.stdout.getvalue(), s2_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            s3.display()
            self.assertEqual(sys.stdout.getvalue(), s3_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_save_to_file_none(self):
        """Test that `save_to_file()` method of Square instance"""
        Base._Base__nb_object = 0
        r1 = Square(10, 2, 8)
        r2 = Square(2)
        Square.save_to_file(None)
        self.assertIs(os.path.exists("Square.json"), True)
        with open("Square.json", 'r') as f:
            self.assertEqual(json.loads(f.read()),
                             json.loads('[]'))
        os.remove("Square.json")

    def test_save_to_file_mt_list(self):
        """Test that `save_to_file()` method of Square instance"""
        Base._Base__nb_object = 0
        r1 = Square(10, 2, 8)
        r2 = Square(2)
        Square.save_to_file([])
        self.assertIs(os.path.exists("Square.json"), True)
        with open("Square.json", 'r') as f:
            self.assertEqual(json.loads(f.read()),
                             json.loads('[]'))
        os.remove("Square.json")
