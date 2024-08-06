#!/usr/bin/env python

import ic
import unittest


tests = (
    ('standard', [1, 0, 10], [10, [(1, 2)]]),
    ('negative', [1, -1, 10], [11, [(1, 2)]]),
    ('no_profit0', [1, -1, -1], [0, [(1, 2)]]),
    ('no_profit1', [1, 1, -1, -1, -2, -2], [0, [(0, 1), (2, 3), (4, 5)]]),
    ('forced_loss', [100, 90, 20, 10], [-10, [(0, 1), (2, 3)]]),
    ('no_shorting', [7, 8, 0], [1, [(0, 1)]]), # can't short at 8 and cover at 0
    ('multiple', [0, 2, 2, 4, 0, 4], [4, [(0, 3), (0, 5), (4, 5)]]),
)
tests_error = (
    ('empty', []),
    ('single0', [0]),
    ('single1', [1]),
)

class TestQ1(unittest.TestCase):

    def test(self):
        for name, input, expected in tests:
            with self.subTest(name=name):
                expected[1] = set(expected[1])
                actual = ic.max_profit(input)
                self.assertEqual(actual, tuple(expected))

    def test_error_empty(self):
        self.assertRaises(ValueError, lambda: ic.max_profit([]))

    def test_error_single(self):
        self.assertRaises(ValueError, lambda: ic.max_profit([0]))
