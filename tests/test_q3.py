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

    def test_gotcha(self):
        self.check([-10, -10, 1, 3, 2], 300, {-10, -10, 3})

    def test_example(self):
        self.check([1, 10, -5, 1, -100], 5000, {10, -5, -100})

    def test_negative_odd(self):
        self.check(
            [-1, -2, -3, -2, -6, -4], -4, {-1, -2, -2})

    def test_negative_odd_with_zero(self):
        self.check(
            [-1, -2, -3, -2, -6, -4, 0], 0, None)

    def test_single(self):
        self.check([-1], -1, {-1}, K=1)

    def test_all(self):
        self.check([-1, 1, 2, -2, 3], 12, {-1, 1, 2, -2, 3}, K=5)
