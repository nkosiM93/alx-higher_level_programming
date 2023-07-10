#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer
import unittest
"""
    Testing modeule for our max_integer 
    module
    """


class TestMaxInt(unittest.TestCase):
    """Tests cases that use the max_integer function"""
    def testEmpty(self):
        self.assertEqual(max_integer([]), None)
    def testCorrect(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def testTwo(self):
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
    def testthree(self):
        self.assertEqual(max_integer([-1, 0, -4, -3]), 0)
    def testFour(self):
        self.assertEqual(max_integer([-1, 0, ord('A'), -3]), 65)
