#!/usr/bin/env python

import ic
import unittest


tests = [
    ('given0', '{[]()}', 1),
    ('given1', '{[(])}', 0),
    ('given2', '{[}', 0),

    ('filter', 'a{b[c]d(e)f}g', 1),

    ('empty', '', 1),

    ('close_fail', ')', 0),

    ('unclosed0', '(', 0),
    ('unclosed1', '(()', 0),
    ('unclosed2', '()(', 0),

    ('ruby_0_0', '|', 0),
    ('ruby_0_1', '|(', 0),
    ('ruby_0_2', '|)', 0),
    ('ruby_0_3', '(|', 0),
    ('ruby_0_4', ')|', 0),
    ('ruby_0_5', '(|)|', 0),
    ('ruby_0_6', '|(|)', 0),
    ('ruby_0_7', '|||', 0),
    ('ruby_0_8', '(|||)', 0),

    ('ruby_1_0', '||', 1),
    ('ruby_1_1', '(||)', 1),
    ('ruby_1_2', '|(||)|', 1),
    ('ruby_1_3', '||(||)', 1),
    ('ruby_1_4', '(||)||', 1),

    ('ruby_2_0', '||||', 2),
    ('ruby_2_1', '|()|||', 2),
    ('ruby_2_2', '||()||', 2),
    ('ruby_2_3', '|||()|', 2),
    ('ruby_2_4', '||(||)||', 2),
]

class TestQ29(unittest.TestCase):
    def test(self):
        for name, input, expected in tests:
            with self.subTest(name=name):
                self.assertEqual(ic.validate_brackets(input), expected)
