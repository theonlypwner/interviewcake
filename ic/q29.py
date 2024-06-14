#!/usr/bin/env python
# Question 29: Bracket Validator (bracket-validator)


def cat(n):
    for i in range(len(cat.cache), n + 1):
        cat.cache.append((4 * i - 2) * cat.cache[-1] // (i +1))
    return cat.cache[n]
cat.cache = [1]

def validate_brackets(text):
    """For a string containing only ([{|}]), checks that all brackets are matched.

    Returns the number of possible ways to parse (0 for invalid).

    Complexity: n = len(text)
    O(n) time
    O(d) space, for depth d of nested brackets
    """

    # filter text
    text = [c for c in text if c in '([{|}])']
    text.append('$')

    CLOSERS = {
        '(': ')',
        '[': ']',
        '{': '}',
        '|': '|',
    }

    unclosed = ['$']
    count = 1

    for c in text:
        if c in CLOSERS:
            unclosed.append(CLOSERS[c])
            continue

        # handle open |
        popped = 0
        while unclosed and unclosed[-1] == '|':
            unclosed.pop()
            popped += 1

        if popped & 1:
            # odd number of |
            return 0

        # number of ways to parse 2n | characters
        # = number of distinct Dyck words with exactly n pairs of parentheses
        # = nth Catalan number
        count *= cat(popped >> 1)

        if not (unclosed and unclosed.pop() == c):
            # unexpected closing, or unclosed at end of string
            return 0

    return count
