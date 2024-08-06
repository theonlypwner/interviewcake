#!/usr/bin/env python
# Question 4: Merging Meeting Times (merging-ranges)


def union_ranges(ranges):
    """Return the union of an iterable of (start, end) pairs.

    Complexity:
    O(n log n) time
    O(n) space for input and output
    """
    result = []
    for s, e in sorted(ranges):
        if result and result[-1][1] >= s:
            result[-1][1] = max(result[-1][1], e)
        else:
            result.append([s, e])

    # convert lists to tuples
    result = list(map(tuple, result))

    return result

def union_ranges2(ranges):
    """Return the union of an iterable of (start, end) pairs.
    max(end) - min(start) must be bounded by a small constant W.

    Complexity:
    O(nW) time
    O(W) space for input and output
    """
    lo = min(map(min, ranges)) if ranges else 0
    hi = max(map(max, ranges)) if ranges else 0

    included = [False] * (hi - lo)
    for s, e in sorted(ranges):
        for i in range(s, e):
            included[i - lo] = True

    # convert lists to tuples
    result = []
    prev = 0
    for i, v in enumerate(included):
        if v:
            if i and not included[i - 1]:
                prev = i
            if i + 1 == len(included) or not included[i + 1]:
                result.append((lo + prev, lo + i + 1))

    return result
