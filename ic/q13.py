#!/usr/bin/env python
# Question 13: Find Rotation Point (find-rotation-point)


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
