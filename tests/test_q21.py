#!/usr/bin/env python

import ic
import unittest


class TestQ21(unittest.TestCase):

    def test(self):
        self.assertEqual(ic.unique_id([1]), 1)
        self.assertEqual(ic.unique_id([1, 2, 2]), 1)
        self.assertEqual(ic.unique_id([1, 2, 2, 3, 3]), 1)
