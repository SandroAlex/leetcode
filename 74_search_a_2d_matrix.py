"""
Search a 2D Matrix - solution review
====================================

Correct and optimal. It treats the matrix as one sorted array of length m*n and
binary-searches it, mapping a flat index back with `divmod(mid, n)`
(`mid // n`, `mid % n`). O(log(m*n)) time, O(1) space, exactly what the problem
asks for. `matrix[0]` is safe because the constraints give m, n >= 1.

Observations
------------
1. `mid` is computed in three places: once before the loop (line 14) and again
   at the end of each branch (lines 33, 38). Compute it once at the top of the
   loop instead:
       while low <= high:
           mid = (low + high) // 2
           ...
   That removes the pre-loop initialization and both duplicated updates.
2. `(low + high) // 2` is fine in Python (no integer overflow), no need for the
   `low + (high - low) // 2` form.
3. The `if number == target` / `if number < target` / `else` chain reads
   slightly better as `if / elif / else`, since the three cases are exclusive.
4. Test coverage is thin: both cases use the same matrix. Worth adding
   target below matrix[0][0], target above the last element, a single-row
   matrix, and a 1x1 matrix.

Suggested revision (same algorithm, less repetition)
---------------------------------------------------
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        while low <= high:
            mid = (low + high) // 2
            value = matrix[mid // n][mid % n]
            if value == target:
                return True
            if value < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Matrix size
        m: int = len(matrix)
        n: int = len(matrix[0])

        # Pseudo 1d matrix
        low: int = 0
        high: int = m * n - 1
        mid: int = (low + high) // 2

        # Binary search in pseudo 1d array
        while low <= high:

            # Calculate matrix indexes for mid value
            i: int = mid // n
            j: int = mid % n

            # Current matrix position
            number: int = matrix[i][j]

            # FounD target
            if number == target:
                return True

            # Target is at right
            if number < target:
                low = mid + 1
                mid = (low + high) // 2

            # Target is at left
            else:
                high = mid - 1
                mid = (low + high) // 2

        return False


if __name__ == "__main__":

    matrix1: List[List[int]] = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target1: int = 3
    out1: bool = True
    assert (
        Solution().searchMatrix(matrix=matrix1, target=target1) == out1
    ), "Case 1 failed!"

    # Test case 2
    matrix2: List[List[int]] = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target2: int = 13
    out2: bool = False
    assert (
        Solution().searchMatrix(matrix=matrix2, target=target2) == out2
    ), "Case 2 failed!"

    print(">>> All tests run successfully!")
