"""
Climbing Stairs - solution review
=================================

The implementation is correct. It is the classic Fibonacci recurrence
(ways(n) = ways(n-1) + ways(n-2)) solved bottom-up with a DP table, running in
O(n) time and O(n) space. Clear and well commented.

Observations
------------
1. O(1) space is enough. Only the previous two values are ever read, so two
   rolling integers replace the length-n table.
2. Redundant `if n > 2` guard. After the `n == 1` and `n == 2` early returns,
   n is always > 2 (constraints give 1 <= n <= 45), so a plain `else` / final
   block is enough. As written, the method has an implicit `return None` path
   for n <= 0, which contradicts the `-> int` annotation.
3. Minor: `s = [1] * n` then `s[0] = 1` - the `s[0] = 1` line is a no-op since
   the list is already filled with 1s.

Suggested O(1)-space revision
-----------------------------
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev, curr = 1, 2  # ways to reach step 1 and step 2
        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr

        return curr

Same O(n) time, constant space, and no unreachable return path.
"""

from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:

        # Very simple case n==1:
        if n == 1:
            return 1

        # Very simple case n==2:
        if n == 2:
            return 2

        # General case n>=2:
        if n > 2:

            # Create a table for storing results
            s: List[int] = [1] * n
            s[0] = 1  # n = 1
            s[1] = 2  # n = 2

            # Fill remaing results
            for i in range(2, n):
                s[i] = s[i - 1] + s[i - 2]

            return s[n - 1]
