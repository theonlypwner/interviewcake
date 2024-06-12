#!/usr/bin/env python

import ic
import unittest


class TestQ2(unittest.TestCase):

    def check(self, array, result):
        self.assertEqual(
            ic.get_products_of_all_ints_except_at_index(array), result)
        self.assertEqual(
            ic.get_products_of_all_ints_except_at_index2(array), result)

    def test_given(self):
        self.check([1, 7, 3, 4], [84, 12, 28, 21])

    def test_example2(self):
        self.check([1, 2, 6, 5, 9], [540, 270, 90, 108, 60])

    def test_example3(self):
        # The solution to this one was not posted in the question
        self.check([3, 1, 2, 5, 6, 4], [240, 720, 360, 144, 120, 180])

    def test_example4(self):
        self.check([2, 4, 10], [40, 20, 8])

    def test_zero1(self):
        self.check([1, 0, 1], [0, 1, 0])

    def test_zero2(self):
        self.check([1, 0, 0], [0, 0, 0])
