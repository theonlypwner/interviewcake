#!/usr/bin/env python

import ic
import unittest


class TestQ1(unittest.TestCase):

    def check(self, input, output):
        output[1] = set(output[1])
        self.assertEqual(ic.max_profit(input), tuple(output))

    def test_empty(self):
        self.assertRaises(ValueError, lambda: ic.max_profit([]))

    def test_single(self):
        self.assertRaises(ValueError, lambda: ic.max_profit([0]))

    def test_standard(self):
        self.check([1, 0, 10], [10, [(1, 2)]])

    def test_negative(self):
        self.check([1, -1, 10], [11, [(1, 2)]])

    def test_no_profit(self):
        self.check([1, -1, -1], [0, [(1, 2)]])
        self.check([1, 1, -1, -1, -2, -2], [0, [(0, 1), (2, 3), (4, 5)]])

    def test_forced_loss(self):
        self.check([100, 90, 20, 10], [-10, [(0, 1), (2, 3)]])

    def test_no_shorting(self):
        # can't short at 8 and cover at 0
        self.check([7, 8, 0], [1, [(0, 1)]])

    def test_multiple(self):
        self.check([0, 2, 2, 4, 0, 4], [4, [(0, 3), (0, 5), (4, 5)]])
