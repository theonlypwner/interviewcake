#!/usr/bin/env python

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
