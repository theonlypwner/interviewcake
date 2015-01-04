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


class TestQ6(unittest.TestCase):

    def check(self, output, *input):
        self.assertEqual(ic.orthotope_intersection(*input), output)

    def test_no_orthotope(self):
        self.assertRaises(ValueError, lambda: ic.orthotope_intersection())

    def test_improper_dimensions(self):
        self.assertRaises(ValueError, lambda: ic.orthotope_intersection(
            ((1, 1), (1, 1)), ((1, 1, 1), (1, 1, 1))
        ))

    def test_improper_coordinate_order(self):
        self.assertRaises(ValueError, lambda: ic.orthotope_intersection(
            ((1, 1), (0, 0)), ((2, 2), (1, 1))
        ))

    def test_one(self):
        self.assertRaises(ValueError, lambda: ic.orthotope_intersection(
            ((0, 0), (1, 1))
        ))

    def test_overlap(self):
        self.check(((1, 1), (3, 3)), ((0, 0), (3, 3)), ((1, 1), (4, 4)))
        self.check(((1, 2), (2, 3)),
                   ((0, 0), (3, 3)), ((1, 1), (4, 4)), ((0, 2), (2, 5)))

    def test_contained(self):
        self.check(((1, 1), (2, 2)), ((0, 0), (9, 9)), ((1, 1), (2, 2)))
        self.check(((2, 3, 4), (3, 4, 5)),
                   ((0, 1, 2), (5, 6, 7)),
                   ((1, 2, 3), (4, 5, 6)),
                   ((2, 3, 4), (3, 4, 5)))

    def test_gap(self):
        self.check(None, ((0, 0), (1, 1)), ((2, 0), (3, 3)))
        self.check(None,
                   ((0, 0, 0, 0), (1, 1, 0, 0)),
                   ((2, 0, 0, 0), (3, 3, 0, 0)),
                   ((0, 0, 0, 0), (9, 9, 9, 9)))

    def test_touch(self):
        self.check(((1, 1), (1, 2)), ((1, 1), (1, 2)), ((1, 1), (2, 3)))
        self.check(((2, 2), (2, 2)),
                   ((0, 0), (2, 2)), ((1, 1), (3, 3)), ((2, 2), (4, 4)))
        self.check(((0, 0), (0, 0)),
                   ((-1, -1), (0, 0)),
                   ((0, 0), (1, 1)),
                   ((-1, -1), (0, 0)),
                   ((0, 0), (1, 1)))


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
