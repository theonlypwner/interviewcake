#!/usr/bin/env python
# Question 29: Bracket Validator (bracket-validator)


def validate_brackets(text):
    """For a string containing only ([{|}]), checks that all brackets are matched.

    Returns 0 for invalid, 1 for unambiguous, and 2 for ambiguous.

    For example, ( and ) are invalid, ([||]) is unambiguous, and
    |||| and ||()|| are ambiguous.

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
    ambiguous = False

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
        elif popped > 2:
            # multiple || pairs
            ambiguous = True

        if not (unclosed and unclosed.pop() == c):
            # unexpected closing, or unclosed at end of string
            return 0

    return 2 if ambiguous else 1
