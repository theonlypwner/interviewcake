#!/usr/bin/env python

import ic
import unittest


class TestQ13(unittest.TestCase):

    def check(self, output, input):
        self.assertEqual(ic.find_rotation_point(input), output)
        # Unrotated input
        self.assertEqual(
            ic.find_rotation_point(input[output:] + input[:output]), 0)

    def test_given(self):
        self.check(5, [
            'ptolemaic',
            'retrograde',
            'supplant',
            'undulate',
            'xenoepist',
            'asymptote',  # <-- rotates here!
            'babka',
            'banoffee',
            'engender',
            'karpatka',
            'othellolagkage',
        ])

    def test_example2(self):
        self.check(2, ['k', 'v', 'a', 'b', 'c', 'd', 'e', 'g', 'i'])

    def test_last(self):
        self.check(3, ['b', 'c', 'd', 'a'])
