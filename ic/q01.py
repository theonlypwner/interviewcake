#!/usr/bin/env python
# Question 1: Apple Stocks (stock-price)


def max_profit(prices):
    """Computes the maximum profit from one buy and one sale trade,
    and a set of all possible trade pairs.

    The input must contain at least 2 prices, and one trade must be done,
    even if it results in a loss.

    Complexity: n=len(stockPricesYesterday)
    O(n) time*
    O(1) auxiliary space for profit amount
    O(n) worst case, O(1) best case space for trade times

    * O(n^2) worst case for building the trade set
    """

    if len(prices) < 2:
        raise ValueError("stockPricesYesterday must not be empty")

    max_profit = prices[1] - prices[0]  # could be negative
    trades = set()

    min_so_far = prices[0]
    min_positions = [0]

    for i in range(1, len(prices)):
        price = prices[i]

        current_profit = price - min_so_far

        # Update best profit
        if current_profit > max_profit:
            # Reset maximum profit amount
            max_profit = current_profit
            trades.clear()
        if current_profit == max_profit:
            # Add all possible trades
            trades |= {(start, i) for start in min_positions if start != i}

        # Track every possible minimum price position so far
        if price < min_so_far:
            min_so_far = price
            min_positions.clear()
        if price == min_so_far:
            min_positions.append(i)

    return max_profit, trades
