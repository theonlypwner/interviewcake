#!/usr/bin/env python

import ic
import unittest


tests = (
    ('gotcha', 3, [-10, -10, 1, 3, 2], 300, [-10, -10, 3]),
    ('example', 3, [1, 10, -5, 1, -100], 5000, [10, -5, -100]),
    ('zeros', 3, [0, 0, 0, 1, -100], 0),
    ('zeros_all', 3, [0, 0, 0, 0, 0], 0, [0, 0, 0]),
    ('negative_odd', 3, [-1, -2, -3, -2, -6, -4], -4, [-1, -2, -2]),
    ('negative_odd_with_zero', 3, [-1, -2, -3, -2, -6, -4, 0], 0),
    ('swap_small_pos_big_neg', 3, [-5, 4, 3, -2, 1, 0], 40, [-5, 4, -2]),
    ('swap_small_neg_big_pos', 3, [5, 4, -3, 2, -1, 0], 40, [5, 4, 2]),
    ('swap_no_neg_outside', 3, [-5, 4, 3, 2, 1], 24, [2, 4, 3]),
    ('swap_no_pos_outside', 3, [5, 4, -3, -2, -1], 30, [5, -2, -3]),
    ('swap_no_pos_inside', 3, [-5, -4, -3, 2, 1], 40, [-5, -4, 2]),
    ('single', 1, [-1], -1, [-1]),
    ('all', 5, [-1, 1, 2, -2, 3], 12, [-1, 1, 2, -2, 3]),
    ('multiple_solutions0', 3, [2, 2, -2, 1, -1, 0], 4, [[2, 2, 1], [2, -2, -1]]),
    ('multiple_solutions1', 3, [2, 2, 2, -2, -2, 0], 8, ((2, 2, 2), (2, -2, -2))),
    # from https://stackoverflow.com/a/42153733/548194
    ('so_a0', 4, [1, 2, 3, 4, 5, 6, 7, 8], 1680, [5, 6, 7, 8]),
    ('so_a1', 4, [1, -2, 3, 4, 5, 100, 2, 3, 1], 6000, [3, 4, 5, 100]),
    ('so_a2', 4, [-10, -10, 1, 3, 2], 600, [2, 3, -10, -10]),
    ('so_a3', 4, [1000, 7, -6, 2, 2], 28000, [1000, 7, 2, 2]),
    ('so_a4', 2, [-1, 0, 1], 0),
    ('so_a5', 4, [2, 5, 8, 9, 1, 3, 7], 2520, [5, 7, 8, 9]),
    ('so_a6', 2, [-1, -1, 2, 1], 2, [2, 1]),
    ('so_a7', 2, [-1000, -1, 2, 3], 1000, [-1, -1000]),
    ('so_a8', 2, [3, 5, 2, 8, 3], 40, [5, 8]),
    ('so_a9', 2, [-1000, -1, 2, 3, 4, 5, 6, 7], 1000, [-1, -1000]),
    # from https://stackoverflow.com/q/22104635/548194
    ('so_b0', 3, [4, 1, -7, -8, 9], 504, [-7, -8, 9]),
    ('so_b1', 3, [1, 3, -6, 3, 5], 45, [3, 3, 5]),
    # from interviewcake sample code
    ('ic_short_list', 3, [1, 2, 3, 4], 24),
    ('ic_longer_list', 3, [6, 1, 3, 5, 7, 8, 2], 336),
    ('ic_list_has_one_negative', 3, [-5, 4, 8, 2, 3], 96),
    ('ic_list_has_two_negatives', 3, [-10, 1, 3, 2, -10], 300),
    ('ic_list_is_all_negatives', 3, [-5, -1, -3, -2], -6),
)

tests_error = (
    ('k_zero', [1], 0, ValueError, 'K must be at least 1'),
    ('k_big_1_2', [1], 2, ValueError, 'List does not contain at least K elements'),
    ('k_big_1_3', [1], 3, ValueError, 'List does not contain at least K elements'),
    ('k_big_2_3', [1, 1], 3, ValueError, 'List does not contain at least K elements'),
)

class TestQ3(unittest.TestCase):

    def check(self, K, array, expected, expected_list=None):
        actual = ic.highest_product(array, K)
        self.assertEqual(actual, expected)

        actual, actual_list = ic.highest_product2(array, K)
        self.assertEqual(actual, expected)
        if expected_list:
            if hasattr(expected_list[0], '__iter__'):
                # multiple solutions
                self.assertIn(sorted(actual_list), map(sorted, expected_list))
            else:
                self.assertCountEqual(actual_list, expected_list)

    def check_fail(self, array, K, exception_type, exception_message):
        with self.assertRaises(exception_type) as context:
            ic.highest_product(array, K)

        self.assertIn(exception_message, context.exception.args[0])

        with self.assertRaises(exception_type) as context:
            ic.highest_product2(array, K)

        self.assertIn(exception_message, context.exception.args[0])

    def test(self):
        for test in tests:
            with self.subTest(name=test[0]):
                self.check(*test[1:])

    def test_error(self):
        for test in tests_error:
            with self.subTest(name=test[0]):
                self.check_fail(*test[1:])
