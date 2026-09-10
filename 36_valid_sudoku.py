"""
Valid Sudoku - solution review
==============================

The current implementation is correct and passes all cases. Since the board is
fixed at 9x9, it runs in O(1) time and space. It is readable and well
commented. The notes below are about efficiency and idiom, not correctness.

Observations
------------
1. Three separate passes. `_sanity1`, `_sanity2` and `_sanity3` each traverse
   the board independently. Rows, columns and 3x3 boxes can all be validated
   in a single pass over the 81 cells.
2. Membership test against a list. `value in current_values` is a linear scan
   (O(9)); a `set` makes it O(1) and is the right structure for "have I seen
   this value?".
3. Instance state. Stashing the grid on `self.board` so the `_sanity*` helpers
   can read it makes the method non-reentrant for no benefit; passing the board
   as an argument (or keeping everything in one method) is cleaner.
4. `if cond: return True else: return False` reduces to `return cond`.

Suggested single-pass revision
------------------------------
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue

                b = (r // 3) * 3 + c // 3
                if value in rows[r] or value in cols[c] or value in boxes[b]:
                    return False

                rows[r].add(value)
                cols[c].add(value)
                boxes[b].add(value)

        return True

Same asymptotic class, but one traversal instead of three and O(1) membership
checks. The box index (r // 3) * 3 + c // 3 maps each cell to one of nine boxes.
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Initialization
        self.board = board

        # Return validity of the table
        if (self._sanity1()) and (self._sanity2()) and (self._sanity3()):
            return True
        else:
            return False

    def _sanity1(self) -> bool:
        """
        Test validity in each row
        """
        
        # Loop over all columns
        for row in range(9):

            # Current values in the row
            current_values: List[str] = []

            # Grab current line       
            line: List[str] = self.board[row]

            # Loop over all columns
            for value in line:

                # Skip void cells
                if value != ".":

                    # Invalid row
                    if value in current_values:
                        return False

                    # Add value being tested
                    current_values.append(value)

        # All rows OK!
        return True

    def _sanity2(self) -> bool:
        """
        Test validity in each column
        """

        # Loop over all columns
        for column in range(9):

            # Current values in the column
            current_values: List[str] = []

            # Loop over all rows
            for row in range(9):

                # Grab value
                value: str = self.board[row][column]

                # Skip void cells
                if value != ".":

                    # Invalid column
                    if value in current_values:
                        return False

                    # Add current valu to teste values
                    current_values.append(value)

        # All columns OK!
        return True

    def _sanity3(self) -> bool:
        """
        Test validity in each sub box
        """

        # Loop over all 3x3 sub boxes
        for sub_row in range(3):
            for sub_col in range(3):

                # Left upper index of sub box
                anc_row: int = 3 * sub_row
                anc_col: int = 3 * sub_col

                # Current values in the column
                current_values: List[str] = []

                # Loop inside each sub box 
                for row in range(anc_row, anc_row + 3):
                    for col in range(anc_col, anc_col + 3):

                        # Grab current value
                        value: str = self.board[row][col]

                        # Skip void cells
                        if value != ".":

                            # Invalid column
                            if value in current_values:
                                return False

                            # Add current valu to teste values
                            current_values.append(value)

        # All valid sub boxes
        return True

if __name__ == "__main__":

    # Valid
    case1_input: List[List[str]] = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    case1_output: bool = True

    # Invalid
    case2_input: List[List[str]] = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    case2_output: bool = False

    assert Solution().isValidSudoku(board=case1_input) == case1_output, \
        "Case 1 failed!"
    assert Solution().isValidSudoku(board=case2_input) == case2_output, \
        "Case 2 failed!"

    print(">>> Run completed!")