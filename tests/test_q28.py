#!/usr/bin/env python

import ic
import unittest


given = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
class TestQ28(unittest.TestCase):

    def check(self, text, index, expected):
        self.assertEqual(ic.get_closing_paren(text, index), expected)

    def test_given(self):
        self.check(given, 10, 79)

    def test_given_second(self):
        self.check(given, 28, 46)

    def test_boundary(self):
        self.check("(test(test)test)", 0, 15)

    def test_no_match(self):
        self.check("(()", 0, -1)
