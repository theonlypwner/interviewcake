#!/usr/bin/env python
# Unit Tests for Interview Cake solutions

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import ic
import unittest


class TestQ1(unittest.TestCase):

    def check(self, input, output):
        output[1] = set(output[1])
        self.assertEqual(ic.max_profit(input), tuple(output))

    def test_empty(self):
        self.assertRaises(AssertionError, lambda: ic.max_profit([]))

    def test_standard(self):
        self.check([1, 0, 10], [10, [(1, 2)]])

    def test_negative(self):
        self.check([1, -1, 10], [11, [(1, 2)]])

    def test_no_profit(self):
        self.check([1, -1, -2], [0, []])
        self.check([1, 1, -1, -1, -2, -2], [0, [(0, 1), (2, 3), (4, 5)]])

    def test_no_shorting(self):
        self.check([1000, 0], [0, []])

    def test_multiple(self):
        self.check([0, 2, 2, 4, 0, 4], [4, [(0, 3), (0, 5), (4, 5)]])

class TestQ2(unittest.TestCase):

    def check(self, array, result):
        self.assertEqual(
            ic.get_products_of_all_ints_except_at_index(array), result)
        self.assertEqual(
            ic.get_products_of_all_ints_except_at_index2(array), result)

    def test_given(self):
        self.check([1, 7, 3, 4], [84, 12, 28, 21])

    def test_example2(self):
        self.check([1, 2, 6, 5, 9], [540, 270, 90, 108, 60])

    def test_example3(self):
        # The solution to this one was not posted in the question
        self.check([3, 1, 2, 5, 6, 4], [240, 720, 360, 144, 120, 180])

    def test_example4(self):
        self.check([2, 4, 10], [40, 20, 8])

    def test_zero1(self):
        self.check([1, 0, 1], [0, 1, 0])

    def test_zero2(self):
        self.check([1, 0, 0], [0, 0, 0])

if __name__ == '__main__':
    unittest.main()
