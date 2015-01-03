#!/usr/bin/env python
# Question 1: Apple Stocks (stock-price)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


def max_profit(stockPricesYesterday):
    """Computes the maximum profit from one buy and one sale trade,
    and a set of all possible trade pairs.
    """

    # stockPricesYesterday must not be empty
    assert stockPricesYesterday

    max_profit = 0, set()
    min_so_far = stockPricesYesterday[0], [0]

    for i, price in enumerate(stockPricesYesterday[1:], 1):
        if price < min_so_far[0]:
            min_so_far = price, [i]
            # Since the price decreased, it cannot result in any larger profit
        else:
            # Track every possible minimum position so far
            if price == min_so_far:
                min_so_far[1].append(i)

            current_profit = price - min_so_far[0]

            if current_profit > max_profit[0]:
                # Reset maximum profit amount
                max_profit = current_profit, set()

            if current_profit == max_profit[0]:
                # Add all possible
                for start in min_so_far[1]:
                    max_profit[1].update(set([(start, i)]))

    return max_profit
