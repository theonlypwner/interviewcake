#!/usr/bin/env python

import ic
import unittest


tests = (
    ('given', [1, 7, 3, 4], [84, 12, 28, 21]),
    ('example2', [1, 2, 6, 5, 9], [540, 270, 90, 108, 60]),
    ('example3', [3, 1, 2, 5, 6, 4], [240, 720, 360, 144, 120, 180]), # The solution to this one was not posted in the question
    ('example4', [2, 4, 10], [40, 20, 8]),
    ('zero1', [1, 0, 1], [0, 1, 0]),
    ('zero2', [1, 0, 0], [0, 0, 0]),
)

class TestQ2(unittest.TestCase):

    def check(self, array, result):
        self.assertEqual(
            ic.get_products_of_all_ints_except_at_index(array), result)
        self.assertEqual(
            ic.get_products_of_all_ints_except_at_index2(array), result)

    def test(self):
        for name, input, expected in tests:
            with self.subTest(name=name):
                self.check(input, expected)
