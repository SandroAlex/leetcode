"""
Find Peak Element - solution review
===================================

Correct (verified by trace on all three test cases, including the monotonic
one where the peak sits at the last index), but it does not meet the problem's
own requirement: "You must write an algorithm that runs in O(log n) time." This
is a bidirectional linear scan from the middle outward - it inspects on the
order of n/2 elements in the worst case (a strictly monotonic array, as in
test case 3, walks nearly the whole array before returning), so it is O(n),
not O(log n). A binary search is what the problem is asking for.

Why it stays correct without an explicit bounds check
-------------------------------------------------------
`fidx` and `bidx` never actually run off the array. Because adjacent elements
are guaranteed distinct and the array's virtual boundaries count as -infinity,
if no interior peak has been found by the time a pointer reaches an edge, the
values on the way there must have been monotonically rising toward it - which
makes that edge a peak by definition, so the boundary branch always returns
before the next increment/decrement could go out of range. That said, the loop
condition `(fidx <= size) or (bidx >= -1)` reads as if it were guarding
against exactly that overrun, when what actually prevents it is the algorithm's
mathematical guarantee, not the condition itself - worth a comment, since as
written it is easy to misread as a real bounds check.

Observations
------------
1. Wrong complexity class. O(n) instead of the required O(log n) - this is the
   main issue; see the binary search revision below.
2. The `size == 1` / `size == 2` special cases add code that a uniform binary
   search doesn't need at all.
3. Test coverage never exercises `size == 1` or `size == 2` directly, even
   though the code special-cases them.

Suggested revision - binary search, O(log n) time, O(1) space
---------------------------------------------------------------
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return low

At each step, moving toward the larger neighbor is guaranteed to move toward a
peak (the virtual -infinity boundaries make this safe at the edges too), so
the search space halves every iteration and every array size - including 1
and 2 - is handled without a special case.
"""

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # Size of the list
        size: int = len(nums)

        # Trivial case 1
        if size == 1:
            return 0

        # Trivial case 2
        if size == 2:
            return 0 if nums[0] > nums[1] else 1

        # Forward index initialization
        fidx: int = size // 2

        # Backward index initialization
        bidx: int = size // 2 - 1

        # Transverse in both directions beginning in the middle of the series
        while (fidx <= size) or (bidx >= -1):

            # Not in extreme
            if fidx != size - 1:

                # Found a peak in forward path
                if (nums[fidx] > nums[fidx + 1]) and (nums[fidx - 1] < nums[fidx]):
                    return fidx

            # Last position
            else:
                if nums[fidx - 1] < nums[fidx]:
                    return fidx

            # If not found, then make a pass forward
            fidx += 1

            # Not in extreme
            if bidx != 0:

                # Found a peak in backward pass
                if (nums[bidx] > nums[bidx + 1]) and (nums[bidx - 1] < nums[bidx]):
                    return bidx

            # First position
            else:
                if nums[bidx] > nums[bidx + 1]:
                    return bidx

            # If not found, then make a pass backward
            bidx -= 1


if __name__ == "__main__":

    # Test case 1
    nums1: List[int] = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    outp1: int = 4
    sol1 = Solution().findPeakElement(nums=nums1)
    assert sol1 == outp1, f"Test case 1 failed: expected {outp1}, got {sol1}"

    # Test case 2
    nums2: List[int] = [1, 2, 3, 1]
    outp2: int = 2
    sol2 = Solution().findPeakElement(nums=nums2)
    assert sol2 == outp2, f"Test case 2 failed: expected {outp2}, got {sol2}"

    # Test case 3
    nums3: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    outp3: int = 11
    sol3 = Solution().findPeakElement(nums=nums3)
    assert sol3 == outp3, f"Test case 3 failed: expected {outp3}, got {sol3}"

    print(">>> All tests OK!")
