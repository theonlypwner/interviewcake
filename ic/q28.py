#!/usr/bin/env python
# Question 28: Parenthesis Matching (matching-parens)


def get_closing_paren(text, opening_paren_index):
    """Finds the index of the matching parenthesis. Returns -1 if not found.

    Complexity: n = len(text)
    O(n) time
    O(1) space
    """
    if text[opening_paren_index] != '(':
        return -1

    open_parens = 1

    for i in range(opening_paren_index + 1, len(text)):
        if text[i] == '(':
            open_parens += 1

        elif text[i] == ')':
            open_parens -= 1

            # Found closing parenthesis
            if not open_parens:
                return i

    # No closing parenthesis
    return -1
