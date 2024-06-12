#!/usr/bin/env python
# Question 1: Apple Stocks (stock-price)


def max_profit(stockPricesYesterday):
    """Computes the maximum profit from one buy and one sale trade,
    and a set of all possible trade pairs.

    Complexity: n=len(stockPricesYesterday)
    O(n) time*
    O(1) auxiliary space for profit amount
    O(n) worst case, O(1) best case space for trade times

    * O(n^2) worst case for building the trade set
    """

    if not stockPricesYesterday:
        raise ValueError("stockPricesYesterday must not be empty")

    max_profit = 0
    trades = set()

    min_so_far = stockPricesYesterday[0]
    min_positions = [0]

    for i, price in enumerate(stockPricesYesterday[1:], 1):
        if price < min_so_far:
            min_so_far = price
            min_positions = [i]
            # Since the price decreased, it cannot result in any larger profit
        else:
            # Track every possible minimum position so far
            if price == min_so_far:
                min_positions.append(i)

            current_profit = price - min_so_far

            if current_profit > max_profit:
                # Reset maximum profit amount
                max_profit = current_profit
                trades = set()

            if current_profit == max_profit:
                # Add all possible trades
                for start in min_positions:
                    if start != i:
                        trades.update(set([(start, i)]))

    return max_profit, trades
