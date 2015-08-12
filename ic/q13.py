#!/usr/bin/env python
# Question 13: Find Rotation Point (find-rotation-point)

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


def find_rotation_point(a):
    """Return the index of the first element of a sorted array
    that is rotated any number of times.

    Complexity: n=len(a), O(f) for comparing items
    O(f log n) time
    O(log n) time for constant time compares
    """
    lo = 0
    hi = len(a)  # instead of len(a) - 1, to detect if it is unrotated
    target = a[0]

    while lo + 1 < hi:
        # Check the middle element
        mid = (lo + hi) >> 1

        if a[mid] > target:
            # Too high: search right
            lo = mid
        else:
            # Too low: search left
            hi = mid

    # Now, these are true:
    # hi == lo + 1
    # a[lo] > target
    # a[hi] < target or hi == len(a)

    # "How can we fix our function to return 0 for an unrotated array?"
    if hi == len(a):
        return 0

    return hi
