#!/usr/bin/python3
import unittest
add_integer = __import__('0-add_integer').add_integer

class Test_add(unittest.TestCase):
    '''test the correct outputs'''
    def test_result(self):
        self.assertAlmostEqual(add_integer(1, 2), 3)
        self.assertAlmostEqual(add_integer(100, -2), 98)
        self.assertAlmostEqual(add_integer(2), 100)
        self.assertAlmostEqual(add_integer(100.3, -2), 98)

    def test_values(self):
       self.assertRaises(TypeError, add_integer, 4, "School")
       self.assertRaises(TypeError, add_integer, None)