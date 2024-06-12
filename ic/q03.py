#!/usr/bin/env python
# Question 3: Highest Product of 3 (highest-product-of-3)


def highest_product(list_of_ints, K):
    """Return the maximum product of K elements from a list.

    Complexity: (more suitable for small or fixed K)
    O(nK) time
    O(K) auxiliary space for products
    O(nK) space to return elements (not implemented)

    Example: if K = 3, or any other constant,
    O(n) time
    O(1) auxiliary space for products
    O(n) space to return elements

    Example: if K scales up with n (such as quarter/half of the list)
    O(n^2) time
    O(n) auxiliary space for products
    O(n^2) space to return elements
    """
    if K < 1:
        raise ValueError("K must be at least 1")
    if len(list_of_ints) < K:
        raise ValueError("List does not contain at least K elements")

    # highest_product_of and lowest_product_of
    H = [None] * (K + 1)
    L = [None] * (K + 1)
    H[0] = L[0] = 1

    # To determine which elements are used in the result,
    # track predecessors and backtrack at the end.
    #
    # This is not implemented here.

    for i, item in enumerate(list_of_ints):
        for n in range(min(K, i + 1), 0, -1):
            a = H[n-1] * item
            b = L[n-1] * item

            if i + 1 == n:
                H[n] = max(a, b)
                L[n] = min(a, b)
            else:
                H[n] = max(H[n], a, b)
                L[n] = min(L[n], a, b)

    return H[K]


def partition_array(array, k, key):
    # TODO implement introselect
    array.sort(key=key)


def product_of(list_input):
    # return reduce(operator.mul, list_input, 1)
    p = 1
    for v in list_input:
        p *= v
    return p

def highest_product2(list_of_ints, K):
    """Return a tuple containing the maximum product of K elements from a list,
    and a return one possible solution for the K elements.

    Refer to https://stackoverflow.com/a/42153733/548194

    Complexity: (optimal for large K)
    O(n) time
    O(log n) auxiliary space for introselect
    O(K) auxiliary space for elements

    Example: if K scales up with n (such as quarter/half of the array)
    O(n) time
    O(log n) auxiliary space for introselect
    O(n) auxiliary space for elements
    """
    if K < 1:
        raise ValueError("K must be at least 1")
    if len(list_of_ints) < K:
        raise ValueError("List does not contain at least K elements")

    if K == len(list_of_ints):
        # answer is same as input
        result = product_of(list_of_ints)
        return result, list_of_ints[:]

    if K & 1 and all(v <= 0 for v in list_of_ints):
        # odd, all non-positive, take least negative values
        partition_array(list_of_ints, K, key = lambda value: -value)
        answer = list_of_ints[:K]
        return product_of(answer), answer

    partition_array(list_of_ints, K, key = lambda value: -abs(value))

    candidate = list_of_ints[:K]
    result = product_of(candidate)
    if result >= 0:
        return result, candidate

    # fix sign: swap maximum - (smallest -) with maximum (biggest +)
    i = max((v, i) for i, v in enumerate(candidate) if v < 0)[1]
    candidate[i] = max(list_of_ints[K:])
    result = product_of(candidate)

    # check alternative: swap minimum + (smallest +) with minimum (biggest -)
    if any(v > 0 for v in list_of_ints[:K]):
        candidate2 = list_of_ints[:K]
        i = min((v, i) for i, v in enumerate(candidate2) if v > 0)[1]
        candidate2[i] = min(list_of_ints[K:])
        result2 = product_of(candidate2)

        if result2 > result:
            return result2, candidate2

    return result, candidate
