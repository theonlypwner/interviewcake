#!/usr/bin/env python
# Question 2: Product of All Other Numbers (product-of-other-numbers)

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


def get_products_of_all_ints_except_at_index(a):
    """Compute an array with each entry replaced by the product
    of all other entries.
    """
    answer = [1] * len(a)

    # Build array containing values of products to the left
    for i in range(len(a) - 1):
        answer[i + 1] = answer[i] * a[i]
    # Note: an accumulator variable is used in the second part but not here,
    # but a local accumulator variable could be potentially accessed faster
    # than the array.

    # Store the result as the array of products to the right is built
    accum = 1
    i = len(a) - 2  # second-last entry
    while i >= 0:
        accum *= a[i + 1]
        answer[i] *= accum
        i -= 1

    return answer


def get_products_of_all_ints_except_at_index2(a):
    """Bonus: What if you could use division? Careful-watch out for zeroes!"""

    # Search for a zero
    zeroIndex = -1
    for i, v in enumerate(a):
        if v == 0:
            zeroIndex = i
            break

    if zeroIndex != -1:  # a zero is in the array
        # Everything is zero except for the item at zeroIndex, which
        # is the product of all other entries.
        # This also works if there are two zeros in the array, in which case
        # all entries will be zero.
        product = 1
        for i, v in enumerate(a):
            if i != zeroIndex:
                if v:
                    product *= v
                else:
                    # Shortcut when there are two zeros
                    product = 0
                    break

        answer = [0] * len(a)
        answer[zeroIndex] = product

        return answer
    else:  # every element in the array is non-zero
        # Calculate the product of every element
        product = 1
        for v in a:
            product *= v

        answer = [product] * len(a)

        # Divide out each element
        for i in range(len(a)):
            answer[i] //= a[i]

        return answer
