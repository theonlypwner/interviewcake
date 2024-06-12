#!/usr/bin/env python
# Question 29: Bracket Validator (bracket-validator)


def validate_brackets(text):
    """For a string containing only ([{|}]), checks that all brackets are matched.

    Returns 0 for invalid, 1 for unambiguous, and 2 for ambiguous.

    For example, ( and ) are invalid, ([||]) is unambiguous, and
    |||| and ||()|| are ambiguous.

    Complexity: n = len(text)
    O(n) time
    O(n) space
    """

    # filter text
    text = [c for c in text if c in '([{|}])']

    CLOSERS = {
        '(': ')',
        '[': ']',
        '{': '}',
        '|': '|',
    }

    unclosed = []
    ambiguous = False

    def handle_pipes():
        nonlocal ambiguous

        popped = False
        while len(unclosed) >= 2 and unclosed[-1] == '|' == unclosed[-2]:
            unclosed.pop()
            unclosed.pop()

            if popped:
                ambiguous = True
            popped = True

    for c in text:
        if c in CLOSERS:
            unclosed.append(CLOSERS[c])
        else:
            handle_pipes()
            if not (unclosed and unclosed.pop() == c):
                # unexpected closing
                return 0

    handle_pipes()

    if unclosed:
        return 0
    elif ambiguous:
        return 2
    else:
        return 1
