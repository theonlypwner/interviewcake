#!/usr/bin/env python

import ic
import unittest


class TestQ43(unittest.TestCase):

    def check(self, output, *arrays):
        if len(arrays) == 2:
            self.assertEqual(ic.merge_arrays2(*arrays), output)
            self.assertEqual(ic.merge_arrays2(arrays[1], arrays[0]), output)
        self.assertEqual(ic.merge_arrays(*arrays), output)

    def test_given(self):
        my_array     = [3, 4, 6, 10, 11, 15]
        alices_array = [1, 5, 8, 12, 14, 19]
        answer = [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
        self.check(answer, my_array, alices_array)

    def test_bonus(self):
        a = [3, 4, 6, 10, 11, 15]
        b = [1, 5, 8, 12, 14, 19]
        c = [0, 4, 18, 20]
        answer = [0, 1, 3, 4, 4, 5, 6, 8, 10, 11, 12, 14, 15, 18, 19, 20]
        self.check(answer, a, b, c)
