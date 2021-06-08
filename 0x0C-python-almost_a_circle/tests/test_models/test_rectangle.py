#!/usr/bin/python3
"""Unittest for the super class called 'Base'
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Class that declares the test functions to test if the
    'Rectangle' class is working correctly.
    """
    def test_rectangle_class(self):
        """Function with some test cases"""
        r1 = Rectangle(10, 3)
        self.assertEqual(3, r1.height)
        self.assertEqual(10, r1.width)

        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(12, r2.id)
        self.assertEqual(0, r1.x)

    def test_area(self):
        """Testing the area() function"""
        r1 = Rectangle(3, 2)
        self.assertEqual(6, r1.area())
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(56, r2.area())

    def test_update(self):
        """Testing the update() function"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(89, r1.id)
        r1.update(79, 2)
        self.assertEqual(79, r1.id)
        self.assertEqual(2, r1.width)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(89, r1.id)
        self.assertEqual(2, r1.width)
        self.assertEqual(3, r1.height)
        self.assertEqual(4, r1.x)
        self.assertEqual(5, r1.y)

        # update with kwargs
        r2 = Rectangle(5, 5, 5, 5)
        r2.update(height=1)
        self.assertEqual(1, r2.height)
        r2.update(x=1, height=2, y=3, width=4)
        self.assertEqual(1, r2.x)
        self.assertEqual(2, r2.height)
        self.assertEqual(3, r2.y)
        self.assertEqual(4, r2.width)

    def test_to_dictionary(self):
        """Testing to-dictionary() function"""
        r1 = Rectangle(10, 2, 1, 9, 12)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 12,
                                         'height': 2, 'width': 10})
                                         