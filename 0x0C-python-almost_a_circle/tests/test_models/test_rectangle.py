#!/usr/bin/python3
''' Test file for the class recangle'''


import unittest
from models.rectangle import Rectangle

class Test_rectangle(unittest.TestCase):

    def test_firstrect(self):
        r1 = Rectangle(10, 2)
        result = (r1.id)
        self.assertAlmostEquals(result, 1)
