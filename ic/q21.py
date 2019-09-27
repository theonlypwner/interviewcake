#!/usr/bin/env python
# Question 21: The Stolen Breakfast Drone (find-unique-int-among-duplicates)

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


def unique_id(delivery_id_confirmations):
    """Find what element appears exactly once, in an array where other elements appear exactly twice.

    Complexity: n=len(delivery_id_confirmations)
    O(n) time
    O(1) space
    """

    result = 0

    for delivery_id in delivery_id_confirmations:
        result ^= delivery_id

    return result
