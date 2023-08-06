#!/usr/bin/env python

import ic
import unittest


class TestQ3(unittest.TestCase):

    def check(self, array, expected, expected_set, K=3):
        r = ic.highest_product(array, K)
        self.assertEqual(r, expected)

        r, a = ic.highest_product2(array, K)
        self.assertEqual(r, expected)
        if expected_set:
            self.assertEqual(set(a), expected_set)

    def check_fail(self, array, K, exception_type, exception_message):
        with self.assertRaises(exception_type) as context:
            ic.highest_product(array, K)

        self.assertIn(exception_message, context.exception.args[0])

        with self.assertRaises(exception_type) as context:
            ic.highest_product2(array, K)

        self.assertIn(exception_message, context.exception.args[0])

    def test_gotcha(self):
        self.check([-10, -10, 1, 3, 2], 300, {-10, -10, 3})

    def test_example(self):
        self.check([1, 10, -5, 1, -100], 5000, {10, -5, -100})

    def test_zeros(self):
        self.check([0, 0, 0, 1, -100], 0, None)

    def test_negative_odd(self):
        self.check([-1, -2, -3, -2, -6, -4], -4, {-1, -2, -2})

    def test_negative_odd_with_zero(self):
        self.check([-1, -2, -3, -2, -6, -4, 0], 0, None)

    def test_single(self):
        self.check([-1], -1, {-1}, K=1)

    def test_all(self):
        self.check([-1, 1, 2, -2, 3], 12, {-1, 1, 2, -2, 3}, K=5)

    def test_k_zero(self):
        self.check_fail([1], 0, ValueError, 'K must be at least 1')

    def test_k_big(self):
        self.check_fail([1], 2, ValueError, 'List does not contain at least K elements')
