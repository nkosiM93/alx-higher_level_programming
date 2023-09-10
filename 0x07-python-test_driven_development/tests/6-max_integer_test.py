#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class contains test methods for a function that looks for a max int"""

    numbers = [4, 9, -5, 13, 136]

    def test_max_integer(self):
        self.assertEqual(max_integer(self.numbers), 136)
        self.numbers = []
        self.assertEqual(max_integer(self.numbers), None)
        self.numbers = [-4, -9, -5, -13, 0, -136]
        self.assertEqual(max_integer(self.numbers), 0)
