"""
Best Time to Buy and Sell Stock II - solution review
===================================================

The implementation is correct and passes all three cases. It walks the series
once, tracking a running buy price (`my_stock`) that follows the price down and,
whenever the price rises above it, "sells" - adding the gain and rebuying at the
current price. On a rising run this captures each incremental step, which is
exactly the sum of the positive day-to-day differences. O(n) time, O(1) space,
which is optimal.

Observations
------------
1. `min_price` is dead code: assigned on line 14, used only to seed `my_stock`,
   never read again. `my_stock = prices[0]` is enough.
2. Doubly-guarded positivity. `current_profit = max(0, current_price - my_stock)`
   and then `if current_profit > 0` check the same thing twice. Drop the
   `max(0, ...)` (the `if` already guards it) - or drop `current_profit`
   entirely, see below.
3. The whole method is the sum of positive consecutive differences:
       sum(b - a for a, b in zip(prices, prices[1:]) if b > a)
   Same complexity, but no running buy-price state and no sell/rebuy
   bookkeeping to convince yourself is correct. This is the canonical form.
4. `n` exists only to write `range(1, n)`; `for price in prices[1:]` (or the
   `zip` pairing above) removes the index arithmetic.
5. Re-annotating `current_price: int` / `current_profit: int` every iteration is
   non-idiomatic; annotate once at first binding or not at all.
6. Test coverage is good (up-down, monotonic up, monotonic down). A
   single-element case (`[5] -> 0`) would round it out.

Suggested revision
------------------
    def maxProfit(self, prices: List[int]) -> int:
        return sum(
            prices[i] - prices[i - 1]
            for i in range(1, len(prices))
            if prices[i] > prices[i - 1]
        )
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Size of the time series
        n: int = len(prices)

        # Initialize the maximum profit
        max_profit: int = 0

        # Initialize the minimum price and my stock
        min_price: int = prices[0]
        my_stock: int = min_price

        # Loop over the complete time series
        for i in range(1, n):

            # Current price
            current_price: int = prices[i]

            # Buy because the price is lower than the minimum or hold if it is worth it
            my_stock = min(my_stock, current_price)

            # Calculate my current profit
            current_profit: int = max(0, current_price - my_stock)

            # Grow my profit
            if current_profit > 0:
                max_profit = max_profit + current_profit

                # Update my stock
                my_stock = current_price

        return max_profit


if __name__ == "__main__":

    # Test case 1
    prices1: List[int] = [7, 1, 5, 3, 6, 4]
    out1: int = 7
    assert Solution().maxProfit(prices=prices1) == out1, "Case 1 failed!"

    # Test case 2
    prices2: List[int] = [1, 2, 3, 4, 5]
    out2: int = 4
    assert Solution().maxProfit(prices=prices2) == out2, "Case 2 failed!"

    # Test case 3
    prices3: List[int] = [7, 6, 4, 3, 1]
    out3: int = 0
    assert Solution().maxProfit(prices=prices3) == out3, "Case 3 failed!"

    print(">>> All tests run successfully!")
