#!/usr/bin/env python

import ic
import unittest


class TestQ29(unittest.TestCase):

    def check(self, text, expected):
        self.assertEqual(ic.validate_brackets(text), expected)

    def test_given(self):
        self.check('{[]()}', 1)
        self.check('{[(])}', 0)
        self.check('{[}', 0)

    def test_filter(self):
        self.check('a{b[c]d(e)f}g', 1)

    def test_empty(self):
        self.check('', 1)

    def test_close_fail(self):
        self.check(')', 0)

    def test_unclosed(self):
        self.check('(', 0)
        self.check('(()', 0)
        self.check('()(', 0)

    def test_ruby(self):
        self.check('|', 0)
        self.check('|)', 0)
        self.check('(|)|', 0)
        self.check('|(|)', 0)
        self.check('||', 1)
        self.check('(||)', 1)
        self.check('|(||)|', 1)
        self.check('||(||)', 1)
        self.check('(||)||', 1)
        self.check('||||', 2)
        self.check('|()|||', 2)
        self.check('||()||', 2)
        self.check('|||()|', 2)
        self.check('||(||)||', 2)
