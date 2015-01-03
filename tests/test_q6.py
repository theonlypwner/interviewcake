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


class TestQ6Rectangles(unittest.TestCase):

    def check(self, a, b, output):
        self.assertEqual(ic.rectangle_intersection(a, b), output)

    def test_rectangle_overlap(self):
        self.check({
            'x': 0,
            'y': 0,
            'width': 10,
            'height': 10,
        }, {
            'x': 5,
            'y': 5,
            'width': 10,
            'height': 10,
        }, {
            'x': 5,
            'y': 5,
            'width': 5,
            'height': 5,
        })

    def test_rectangle_contained(self):
        self.check({
            'x': 0,
            'y': 0,
            'width': 10,
            'height': 10,
        }, {
            'x': 5,
            'y': 5,
            'width': 5,
            'height': 5,
        }, {
            'x': 5,
            'y': 5,
            'width': 5,
            'height': 5,
        })

    def test_rectangle_gap(self):
        self.check({
            'x': 0,
            'y': 0,
            'width': 10,
            'height': 10,
        }, {
            'x': 11,
            'y': 11,
            'width': 10,
            'height': 10,
        },
            None
        )

    def test_rectangle_touch(self):
        self.check({
            'x': 0,
            'y': 0,
            'width': 10,
            'height': 10,
        }, {
            'x': 10,
            'y': 10,
            'width': 10,
            'height': 10,
        }, {
            'x': 10,
            'y': 10,
            'width': 0,
            'height': 0,
        })
