"""
Best Time to Buy and Sell Stock - solution review
=================================================

The implementation is correct: a single left-to-right pass tracking the minimum
price seen so far and the best profit achievable against it. O(n) time,
O(1) space, which is optimal for this problem.

Observations
------------
1. The `n == 1` / `n == 2` special cases and the two-element initialization are
   not needed. Start with `min_past_price = prices[0]` and `max_profit = 0`,
   then loop from index 1: for n == 1 the loop body never runs and 0 is
   returned automatically. (n >= 1 is guaranteed by the constraints, so
   `prices[0]` is safe.)
2. `max(0, current_price - min_past_price)` is redundant. `max_profit` starts
   at 0 and only ever increases, so comparing the raw difference
   `current_price - min_past_price` is enough.
3. Re-annotating `min_past_price: int = ...` on reassignment inside the loop is
   non-idiomatic; annotate once at first binding, then plain
   `min_past_price = min(...)`.
4. `if current_profit > max_profit: max_profit = current_profit` reads more
   directly as `max_profit = max(max_profit, ...)`.
5. Test coverage: add a single-element case (`[5] -> 0`) and a monotonically
   increasing case (`[1, 2, 3, 4] -> 3`) to exercise the boundaries.

Suggested revision
------------------
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Size of prices list
        n: int = len(prices)

        # Trivial case 1
        if n == 1:
            return 0

        # Trivial case 2
        if n == 2:
            return max(0, prices[1] - prices[0])

        # Initialize the minimum past price for more general case
        min_past_price: int = min(prices[0], prices[1])

        # Intialize final profit for more general case
        max_profit: int = max(0, prices[1] - prices[0])

        # Loop over the remaining time series
        for i in range(2, n):

            # Current price
            current_price: int = prices[i]

            # Current profit
            current_profit: int = max(0, current_price - min_past_price)

            # Update return
            if current_profit > max_profit:
                max_profit = current_profit

            # Update minimum historical value
            min_past_price: int = min(min_past_price, current_price)

        # Maximum profit
        return max_profit


if __name__ == "__main__":

    # Test case 1
    prices1: List[int] = [7, 1, 5, 3, 6, 4]
    out1: int = 5
    assert Solution().maxProfit(prices=prices1) == out1, "Case 1 failed!"

    # Test case 2
    prices2: List[int] = [7, 6, 4, 3, 2, 1]
    out2: int = 0
    assert Solution().maxProfit(prices=prices2) == out2, "Case 2 failed!"

    print(">>> All tests run successfully!")
