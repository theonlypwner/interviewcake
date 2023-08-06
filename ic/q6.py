#!/usr/bin/env python
# Question 6: Rectangular Love (rectangular-love)


def orthotope_intersection(*o):
    """Return the intersection of n-orthotopes, whose format is
    a 2-tuple containing the lower and higher coordinates, respectively.

    If there is no intersection, None is returned.

    Example: ((x1, y1, z1, w1, ...), (x2, y2, z2, w2, ...))
    with x1 <= x2, y1 <= y2, z1 <= z2, ...

    Complexity:
    O(mn) time where m is the number of n-orthotopes
    O(n) auxiliary space
    """
    if len(o) < 2:
        raise ValueError("There must be at least two orthotopes")

    n = len(o[0][0])
    for orthotope in o:
        if n != len(orthotope[0]) or n != len(orthotope[1]):
            raise ValueError("The number of dimensions must be consistent")

        for i in range(n):
            if orthotope[0][i] > orthotope[1][i]:
                raise ValueError("Incorrect coordinate order")

    # lower and upper vertices
    lower = [None] * n
    upper = [None] * n

    for i in range(n):
        lower[i] = max(*(orthotope[0][i] for orthotope in o))
        upper[i] = min(*(orthotope[1][i] for orthotope in o))

        if lower[i] > upper[i]:
            return None

    return (tuple(lower), tuple(upper))


"""Return the intersection of two rectangles, or None if they do not
intersect. The format is ((x1, y1), (x2, y2)) with x1 <= x2, y1 <= y2.
"""
rectangle_intersection_new = orthotope_intersection


def rectangle_intersection(a, b):
    """Return the intersection of two rectangles, or None if they do not
    intersect. The format is specific to the original question.

    Complexity:
    O(1) time
    O(1) auxiliary space
    because n = m = 2
    """

    a = ((a['x'], a['y']), (a['x'] + a['width'], a['y'] + a['height']))
    b = ((b['x'], b['y']), (b['x'] + b['width'], b['y'] + b['height']))
    intersection = rectangle_intersection_new(a, b)

    if intersection is None:
        return None

    return {
        'x': intersection[0][0],
        'y': intersection[0][0],
        'width': intersection[1][0] - intersection[0][0],
        'height': intersection[1][1] - intersection[0][1],
    }
