#!/usr/bin/env python

import ic
import unittest


class TestQ3(unittest.TestCase):

    def check(self, array, expected, expected_list=None, K=3):
        actual = ic.highest_product(array, K)
        self.assertEqual(actual, expected)

        actual, actual_list = ic.highest_product2(array, K)
        self.assertEqual(actual, expected)
        if expected_list:
            self.assertCountEqual(actual_list, expected_list)

    def check_fail(self, array, K, exception_type, exception_message):
        with self.assertRaises(exception_type) as context:
            ic.highest_product(array, K)

        self.assertIn(exception_message, context.exception.args[0])

        with self.assertRaises(exception_type) as context:
            ic.highest_product2(array, K)

        self.assertIn(exception_message, context.exception.args[0])

    def test_gotcha(self):
        self.check([-10, -10, 1, 3, 2], 300, [-10, -10, 3])

    def test_example(self):
        self.check([1, 10, -5, 1, -100], 5000, [10, -5, -100])

    def test_zeros(self):
        self.check([0, 0, 0, 1, -100], 0)

    def test_zeros_all(self):
        self.check([0, 0, 0, 0, 0], 0, [0, 0, 0])

    def test_negative_odd(self):
        self.check([-1, -2, -3, -2, -6, -4], -4, [-1, -2, -2])

    def test_negative_odd_with_zero(self):
        self.check([-1, -2, -3, -2, -6, -4, 0], 0)

    def test_swap_small_pos_big_neg(self):
        self.check([-5, 4, 3, -2, 1, 0], 40, [-5, 4, -2])

    def test_swap_small_neg_big_pos(self):
        self.check([5, 4, -3, 2, -1, 0], 40, [5, 4, 2])

    def test_swap_no_neg_outside(self):
        self.check([-5, 4, 3, 2, 1], 24, [2, 4, 3])

    def test_swap_no_pos_outside(self):
        self.check([5, 4, -3, -2, -1], 30, [5, -2, -3])

    def test_swap_no_pos_inside(self):
        self.check([-5, -4, -3, 2, 1], 40, [-5, -4, 2])

    def test_single(self):
        self.check([-1], -1, [-1], K=1)

    def test_all(self):
        self.check([-1, 1, 2, -2, 3], 12, [-1, 1, 2, -2, 3], K=5)

    def test_k_zero(self):
        self.check_fail([1], 0, ValueError, 'K must be at least 1')

    def test_k_big(self):
        self.check_fail([1], 2, ValueError, 'List does not contain at least K elements')

    def test_extra(self):
        # from https://stackoverflow.com/a/42153733/548194
        self.check([1, 2, 3, 4, 5, 6, 7, 8], 1680, [5, 6, 7, 8], K=4)
        self.check([1, -2, 3, 4, 5, 100, 2, 3, 1], 6000, [3, 4, 5, 100], K=4)
        self.check([-10, -10, 1, 3, 2], 600, [2, 3, -10, -10], K=4)
        self.check([1000, 7, -6, 2, 2], 28000, [1000, 7, 2, 2], K=4)
        self.check([-1, 0, 1], 0, K=2)
        self.check([2, 5, 8, 9, 1, 3, 7], 2520, [5, 7, 8, 9], K=4)
        self.check([-1, -1, 2, 1], 2, [2, 1], K=2)
        self.check([-1000, -1, 2, 3], 1000, [-1, -1000], K=2)
        self.check([3, 5, 2, 8, 3], 40, [5, 8], K=2)
        self.check([-1000, -1, 2, 3, 4, 5, 6, 7], 1000, [-1, -1000], K=2)
        # from https://stackoverflow.com/q/22104635/548194
        self.check([4, 1, -7, -8, 9], 504, [-7, -8, 9])
        self.check([1, 3, -6, 3, 5], 45, [3, 3, 5])
