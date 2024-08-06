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
    # different from 'official' solution
    ('empty', [], []),
    ('single', [0], [1]),
    # from official test cases
    ('ic_small_list', [1, 2, 3], [6, 3, 2]),
    ('ic_longer_list', [8, 2, 4, 3, 1, 5], [120, 480, 240, 320, 960, 192]),
    ('ic_list_has_one_zero', [6, 2, 0, 3], [0, 0, 36, 0]),
    ('ic_list_has_two_zeros', [4, 0, 9, 1, 0], [0, 0, 0, 0, 0]),
    ('ic_one_negative_number', [-3, 8, 4], [32, -12, -24]),
    ('ic_all_negative_numbers', [-7, -1, -4, -2], [-8, -56, -14, -28]),
    # test_error_with_empty_list
    # test_error_with_one_number
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
