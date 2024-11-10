#!/usr/bin/env python

import ic
import unittest


tests = (
    ('example', [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)], [(0, 1), (3, 8), (9, 12)]),
    ('unordered', [(10, 12), (0, 1), (3, 5), (4, 8), (9, 10)], [(0, 1), (3, 8), (9, 12)]),
    ('gotcha_merge', [(1, 2), (2, 3)], [(1, 3)]),
    ('gotcha_subsume', [(1, 5), (2, 3)], [(1, 5)]),
    ('gotcha_multimerge', [(1, 10), (2, 6), (3, 5), (7, 9)], [(1, 10)]),
    ('large', [(1000000000, 2000000000), (1900000000, 3000000000)], [(1000000000, 3000000000)]),
    ('empty', [], []),
)

class TestQ4(unittest.TestCase):

    def check(self, input, output):
        diff = max(map(max, input)) - min(map(min, input)) if input else 0

        self.assertEqual(ic.union_ranges(input), output)
        if diff <= 2 ** 20:
            self.assertEqual(ic.union_ranges2(input), output)

    def test(self):
        for name, input, expected in tests:
            with self.subTest(name=name):
                self.check(input, expected)
