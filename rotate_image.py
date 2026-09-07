"""
Rotate Image - solution review
==============================

The implementation is correct. It rotates 90 degrees clockwise by transposing
the matrix and then reversing each row, entirely in place: O(n^2) time and
O(1) extra space, which is optimal for this problem.

Observations
------------
1. Naming. `_reverse_columns` actually reverses each *row* (it swaps
   matrix[i][j] with matrix[i][size-1-j] for a fixed row i). "reverse_rows"
   would describe it better.
2. Loop over the whole grid then filter. Both helpers iterate all n^2 cells
   and guard with `if i > j` / `if j < size // 2`. Bounding the inner range
   directly does the same work with half the iterations and no branch:
       for i in range(size):
           for j in range(i):              # transpose: lower triangle only
               ...
       for i in range(size):
           for j in range(size // 2):      # reverse row i
               ...
3. Unused loop variables. `row_element` / `row_elements` are never read; only
   the indices are used, so `range` is clearer than `enumerate`.
4. Instance state. `self.matrix` / `self.size` make the method non-reentrant
   for no benefit; locals (or a single method) are cleaner. Note the two
   helpers refer to the size inconsistently - `len(self.matrix)` in one,
   `self.size` in the other.
5. The __main__ block calls `rotate` but asserts nothing; adding expected
   outputs would make it a real self-check.

Suggested tightening (same algorithm, fewer moving parts)
--------------------------------------------------------
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        self.matrix = matrix    
        self.size = len(self.matrix)

        self._transpose()
        self._reverse_columns()

    def _transpose(self):
        for i, row_elements in enumerate(self.matrix):
            for j, row_element in enumerate(row_elements):
                if i > j:
                    
                    # Swap elements
                    self.matrix[i][j], self.matrix[j][i] = \
                        self.matrix[j][i], self.matrix[i][j]

    def _reverse_columns(self):
        for i, row_elements in enumerate(self.matrix):
            for j, row_element in enumerate(row_elements):
                if j < len(self.matrix) // 2:

                    # Swap elements
                    self.matrix[i][j], self.matrix[i][self.size - 1 - j] = \
                        self.matrix[i][self.size - 1 - j], self.matrix[i][j]


if __name__ == "__main__":

    # Input 1
    matrix1: List[List[int]] = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    # Input 2
    matrix2: List[List[int]] = [
        [5,1,9,11],
        [2,4,8,10],
        [13,3,6,7],
        [15,14,12,16]
    ]

    Solution().rotate(matrix=matrix1)
    Solution().rotate(matrix=matrix2)
