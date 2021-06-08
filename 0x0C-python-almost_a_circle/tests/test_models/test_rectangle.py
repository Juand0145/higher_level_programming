#!/usr/bin/python3
'''tst file were are analizing the function of the rectagle'''
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''Tsting the parent class Rectangle'''

    def test_rectangle(self):
        '''Testing the creation of the rectangle'''
        r1 = Rectangle(10, 3)
        self.assertEqual(3, r1.height)
        self.assertEqual(10, r1.width)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(12, r2.id)
        self.assertEqual(0, r1.x)

    def test_area_rectangle(self):
        '''Testing the publci method area were we are finding the
        area of a rectangle'''
        r1 = Rectangle(3, 2)
        self.assertEqual(6, r1.area())
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(56, r2.area())

    def test_update_rectangle(self):
        '''Testing the update method'''
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
        r2 = Rectangle(5, 5, 5, 5)
        r2.update(height=1)
        self.assertEqual(1, r2.height)
        r2.update(x=1, height=2, y=3, width=4)
        self.assertEqual(1, r2.x)
        self.assertEqual(2, r2.height)
        self.assertEqual(3, r2.y)
        self.assertEqual(4, r2.width)

    def test_dictionary(self):
        '''Testing to-dictionary() function'''
        r1 = Rectangle(10, 2, 1, 9, 12)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual
        (r1_dictionary, {'x': 1, 'y': 9, 'id': 12, 'height': 2, 'width': 10})
