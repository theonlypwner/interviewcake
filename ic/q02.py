#!/usr/bin/env python
# Question 2: Product of All Other Numbers (product-of-other-numbers)


def get_products_of_all_ints_except_at_index(a):
    """Compute an array with each entry replaced by the product
    of all other entries.

    An empty array results in an empty array.
    An array with a single element results in an array containing a single 1.

    Complexity: N=len(a)
    O(N) time
    O(N) auxiliary space
    """
    N = len(a)
    answer = [1] * N

    # Build array containing values of products to the left
    for i in range(N - 1):
        answer[i + 1] = answer[i] * a[i]
    # Note: an accumulator variable is used in the second part but not here,
    # but a local accumulator variable could be potentially accessed faster
    # than the array.

    # Store the result as the array of products to the right is built
    accum = 1
    i = N - 2  # second-last entry
    while i >= 0:
        accum *= a[i + 1]
        answer[i] *= accum
        i -= 1

    return answer


def get_products_of_all_ints_except_at_index2(a):
    """Bonus: What if you could use division? Careful-watch out for zeroes!"""

    # Calculate the product of every element before the first 0,
    # and also record the position of the first 0
    product = 1
    zeroIndex = -1
    for i, v in enumerate(a):
        if v == 0:
            zeroIndex = i
            break
        product *= v

    if zeroIndex != -1:  # 0 was found
        # In the answer, everything is 0 except for the item at zeroIndex,
        # which should be the product of all other entries.
        # This also works if there are multiple zeros in the array, in which case
        # all entries will be zero.

        # product is the cumulative product before zeroIndex, so
        # continue to multiply the items to the right of that item
        for i in range(zeroIndex + 1, len(a)):
            if a[i]:
                product *= a[i]
            else:
                # Shortcut for when there are two zeros
                product = 0
                break

        answer = [0] * len(a)
        answer[zeroIndex] = product

        return answer
    else:  # every element in the array is non-zero
        answer = [product] * len(a)

        # Divide out each element
        for i in range(len(a)):
            answer[i] //= a[i]

        return answer
