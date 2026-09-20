"""
Remove Element - solution review
================================

Correct for the four test cases, and the overall approach - swap a match to
the tail and shrink the boundary - is the right idea (O(n) time, O(1) space,
same class as the optimal solution). It still leans on a fragile trick for
its stopping condition (see below).

Observations
------------
1. The sentinel value 51 only works by accident of this problem's own
   constraints (`0 <= nums[i] <= 50`), which the code never states or checks.
   `nums[curidx] == 51` is used to mean "this slot was already marked as
   removed," but that is only true because 51 cannot be a genuine value here.
   Reuse this function with any other value range (or just change the
   constraint) and it silently breaks - it would either stop early on a real
   51 or never stop on a marker that collides with real data.
2. `lasidx` is redundant: at every point in the run, `lasidx == k - 1` (both
   start at `len(nums) - 1` and both decrement together on every removal), so
   the variable can be dropped and `nums[k - 1]` used directly.
3. The `nums[lasidx] = 51` writes are pure overhead - the problem only cares
   about the first k elements, so marking the discarded tail is unnecessary
   work that exists solely to support the sentinel-based stopping check.
4. All of the above goes away by comparing indices instead of values, e.g.
   `while curidx < k`, which is exactly the general, data-independent version
   of the same stopping condition the sentinel was approximating.

(The earlier version of this file had a test bug where case 2 asserted against
leftover variables from case 1 instead of its own; each test case now reuses
and immediately checks its own `nums`/`val`/`outp`/`sol`, so that is fixed.)

Suggested revision
------------------
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        i = 0
        while i < k:
            if nums[i] == val:
                k -= 1
                nums[i] = nums[k]
            else:
                i += 1
        return k

Same swap-with-the-tail idea, but the boundary check is on the index (`i < k`)
rather than on a value that has to be guaranteed absent from the data, so it
is correct for any value range with no sentinel and no extra state.
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # Initialize output
        k: int = len(nums)

        # Last available index of the list
        lasidx: int = len(nums) - 1

        # Current index
        curidx: int = 0

        # This serves as a loop over all available numbers
        while curidx < len(nums):

            # Do not need more iterations
            if nums[curidx] == 51:
                break

            # If the current number is the targe, then swap it to last positions
            while nums[curidx] == val:

                # Swap
                nums[curidx], nums[lasidx] = nums[lasidx], nums[curidx]

                # Last position is now set to an invalid number
                nums[lasidx] = 51

                # Update last index
                lasidx -= 1

                # Update counts
                k -= 1

            # Goes to the next one
            curidx += 1

        return k


if __name__ == "__main__":

    # Test case 1
    nums: List[int] = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    outp: int = 5
    sol = Solution().removeElement(nums=nums, val=val)
    assert sol == outp, f"Test case 1 failed: expected {outp}, got {sol}"

    # Test case 2
    nums: List[int] = [50]
    val = 49
    outp: int = 1
    sol = Solution().removeElement(nums=nums, val=val)
    assert sol == outp, f"Test case 2 failed: expected {outp}, got {sol}"

    # Test case 3
    nums: List[int] = [50]
    val = 50
    outp: int = 0
    sol = Solution().removeElement(nums=nums, val=val)
    assert sol == outp, f"Test case 3 failed: expected {outp}, got {sol}"

    # Test case 4
    nums: List[int] = [3, 2, 2, 3]
    val = 3
    outp: int = 2
    sol = Solution().removeElement(nums=nums, val=val)
    assert sol == outp, f"Test case 4 failed: expected {outp}, got {sol}"
