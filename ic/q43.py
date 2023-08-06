#!/usr/bin/env python
# Question 43: Merge Sorted Arrays (merge-sorted-arrays)


def merge_arrays2(a, b):
    """Combine and return two sorted arrays.

    Complexity: A = len(a), B = len(b)
    O(a + b) time
    O(a + b) space for output
    O(1) space excluding output
    """

    i = 0
    j = 0
    i_max = len(a)
    j_max = len(b)

    result = []

    # Add smallest element so far
    while i < i_max and j < j_max:
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # Add remaining elements of larger array
    while i < i_max:
        result.append(a[i])
        i += 1
    while j < j_max:
        result.append(b[j])
        j += 1

    return result


def merge_arrays(*a):
    """Combine and return multiple sorted arrays.

    Complexity: N = len(a), L = sum(len(x) for x in a)
    O(NL) time
    O(N + L) space
    """

    N = len(a)
    cur_index = [0] * N
    result = []

    # Add smallest element so far
    while True:
        min_array = None

        # Find array with smallest next item
        for array in range(N):
            if cur_index[array] < len(a[array]) and (min_array is None or
                a[array][cur_index[array]] < a[min_array][cur_index[min_array]]):

                min_array = array

        if min_array is None:
            break

        # Add it
        result.append(a[min_array][cur_index[min_array]])
        cur_index[min_array] += 1

    return result
