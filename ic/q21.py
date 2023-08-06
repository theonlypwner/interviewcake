#!/usr/bin/env python
# Question 21: The Stolen Breakfast Drone (find-unique-int-among-duplicates)


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
