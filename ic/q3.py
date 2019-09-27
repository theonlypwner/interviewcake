#!/usr/bin/env python
# Question 3: Highest Product of 3 (highest-product-of-3)

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


def highest_product(a, b):
    pass
'''
def highest_product(array_of_ints, K):
    """Return a tuple containing the maximum product of K elements from an
    array and a set containing all possible sets of K elements.

    Complexity: (more suitable for fixed K)
    O(nK) time
    O(K) auxiliary space for products and indices
    O(n^2) auxiliary space for sets in the worst case

    Example: if K = 3, or any other constant,
    O(n) time
    O(1) auxiliary space for products
    O(n^2) auxiliary space for sets
    """
    if K < 1:
        raise ValueError("K must be at least 1")
    if len(array_of_ints) < K:
        raise ValueError("Array does not contain at least K elements")

    highest_product_of = [None] * K
    possible_sets = set(set(array_of_ints[:K]))

    for i, item in enumerate(array_of_ints):
        for n in range(min(K, i), 0, -1):
            if i == n-1:
                highest_product_of[i] = (..., [i])
            elif True:
                highest_product_of[n-1] = (, +i)

    return (highest_product_of[K-1], possible_sets)'''


def highest_product2(array_of_ints, K):
    """
    Credit: Eyal Schneider http://stackoverflow.com/a/22106558
    but his solution doesn't account for 0 elements

    Complexity: (more suitable for large K)
    O(N log N) time*
    O(K) auxiliary space for products
    O(n^2) auxiliary space for sets in the worst case

    Example: if K scales up with N (e.g. quarter/half of the array)
    O(N log N) time [better than O(N^2) time]
    O(N) auxiliary space for products

    * Since K <= N, O(N log N + N + K) becomes O(N log N)
    """
    if K < 1:
        raise ValueError("K must be at least 1")
    if len(array_of_ints) < K:
        raise ValueError("Array does not contain at least K elements")

    N = len(array_of_ints)
    a = sorted(array_of_ints)

    # Build cumulative product arrays
    lower = [1]
    upper = [1]

    for i, v in enumerate(a):
        if v >= 0:
            break
        lower.append(lower[i] * v)
    for i, v in enumerate(a[-1::-1]):
        if v <= 0:
            break
        upper.append(upper[i] * v)

    L = len(lower)
    U = len(upper)

    max_product = -1000000

    i_min = max(0, (K - U + 1) / 2)
    if i_min & 1:
        i_min += 1
    i_max = min(K, L, U)
    for i in range(i_min, i_max + 1, 2):
        print(a, i)
        max_product = max(max_product, lower[i] * upper[K - i])

    return max_product
