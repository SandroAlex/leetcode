"""
Merge Sorted Array - solution review
====================================

Correct (all four cases pass, including the earlier m == 0 bug now fixed by
the in-place slice assignment `nums1[:] = nums1[:m] + nums2[:n]`). But it is
far from efficient: it is a selection-sort-style merge, not the linear merge
the problem is built for.

Complexity
----------
The first loop runs n times; each iteration rescans `nums1[:m]` for its max
and index (O(m)), rescans the shrinking `nums2` for its max (O(k)), and does
a `list.remove` (O(k)) - so that loop alone is roughly O(n * m + n^2). The
second loop ("bubblesort" in the comment, but it is actually selection sort -
each pass swaps the max of the unsorted prefix to the end) is O(m^2). Overall
this is roughly O(m^2 + n^2 + n*m), i.e. quadratic in the total size, where
the problem has a well-known O(m + n) solution.

Observations
------------
1. Quadratic vs. linear. Both nums1[:m] and nums2 are already individually
   sorted - that fact is never used. Repeatedly taking `max()` of each throws
   away the sortedness and pays for it with an extra O(size) scan every step.
2. The trivial `m == 0` / `n == 0` branch is unnecessary: the standard
   two-pointer merge below handles both automatically, so no special case is
   needed at all.
3. `nums2.remove(max2)` is O(n) per call (linear search + shift) - another
   place where ignoring the existing order costs time that a reverse index
   walk would avoid entirely.
4. Comment says "bubblesort" but the code is selection sort (find the max of
   the unsorted region, swap it to the end). Worth fixing the label since it
   describes the algorithm, not just style.
5. `max()` and `.index()` are each a separate O(m) pass over the same slice;
   even keeping this general approach, tracking (value, index) in one pass
   would halve that constant, though the loop-per-iteration issue in point 1
   is what actually decides the growth rate.

Suggested revision - linear two-pointer merge from the back
------------------------------------------------------------
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

Walking both arrays from their tail and writing the larger remaining value
into the back of nums1 is O(m + n) time and O(1) extra space - optimal, and
it naturally covers m == 0 and n == 0 without a special case.
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Trivial cases. Slice assignment, which mutates in place instead of rebinding
        if (m == 0) or (n == 0):
            nums1[:] = nums1[:m] + nums2[:n]

        else:

            # Last available position
            idx_fill: int = m + n - 1

            # Use all elements of second list
            while idx_fill >= m:

                # Find the maximum of first list
                max1: int = max(nums1[:m])
                idx_max1: int = nums1[:m].index(max1)

                # Find the maximum of second list
                max2: int = max(nums2)

                # Maximum in the second list
                if max2 >= max1:

                    # From second list to the first one
                    nums1[idx_fill] = max2

                # Maximum in the first list
                else:

                    # Swap elements in first list
                    nums1[idx_max1], nums1[idx_fill] = nums1[idx_fill], nums1[idx_max1]

                    # Find the maximum in the second list in put in the swapped position in the first one
                    nums1[idx_max1] = max2

                # Remove from list
                nums2.remove(max2)

                # Go back one position
                idx_fill = idx_fill - 1

            # Apply the bubblesort for the original first list
            while idx_fill > 0:

                # Find max
                max1: int = max(nums1[: idx_fill + 1])
                idx_max1: int = nums1[: idx_fill + 1].index(max1)

                # Swap elements
                nums1[idx_max1], nums1[idx_fill] = nums1[idx_fill], nums1[idx_max1]

                # Go back one position
                idx_fill = idx_fill - 1


if __name__ == "__main__":

    # Test 1
    nums1: List[int] = [1, 2, 3, 0, 0, 0]
    m: int = 3
    nums2: List[int] = [2, 5, 6]
    n: int = 3
    Solution().merge(nums1=nums1, m=m, nums2=nums2, n=n)
    assert nums1 == [1, 2, 2, 3, 5, 6], "Case 1 failed!"

    # Test 2
    nums1: List[int] = [1, 10, 12, 13, 0, 0, 0, 0]
    m: int = 4
    nums2: List[int] = [3, 4, 5, 18]
    n: int = 4
    Solution().merge(nums1=nums1, m=m, nums2=nums2, n=n)
    assert nums1 == [1, 3, 4, 5, 10, 12, 13, 18], "Case 2 failed!"

    # Test 3
    nums1: List[int] = [6, 10, 12, 13, 0, 0, 0, 0]
    m: int = 4
    nums2: List[int] = [3, 4, 5, 18]
    n: int = 4
    Solution().merge(nums1=nums1, m=m, nums2=nums2, n=n)
    assert nums1 == [3, 4, 5, 6, 10, 12, 13, 18], "Case 3 failed!"

    # Test 4
    nums1: List[int] = []
    m: int = 0
    nums2: List[int] = [8]
    n: int = 1
    Solution().merge(nums1=nums1, m=m, nums2=nums2, n=n)
    assert nums1 == [8], "Case 4 failed!"

    print(">>> All tests run successfully!")
