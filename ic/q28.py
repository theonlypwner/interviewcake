#!/usr/bin/env python
# Question 28: Parenthesis Matching (matching-parens)

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


def get_closing_paren(text, opening_paren_index):
    """Finds the index of the matching parenthesis. Returns -1 if not found.

    Complexity: n = len(text)
    O(n) time
    O(1) space
    """
# TODO: "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.", 10 -> 79
    if text[opening_paren_index] != '(':
        return -1

    open_parens = 1

    for i in range(opening_paren_index + 1, len(text)):
        if text[i] == '(':
            open_parens += 1

        elif text[i] == ')':
            open_parens -= 1

            # Found closing parenthesis
            if not open_parens:
                return i

    # No closing parenthesis
    return -1
