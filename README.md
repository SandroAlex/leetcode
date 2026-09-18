# LeetCode Studies

A personal study log of LeetCode problems. For each problem I write my own solution first, then use **Claude Code** to review it and produce a reference ("best practice") version, and I keep both side by side so I can see the gap and learn from it.

## How it works

For every problem there is one Python file, named `<number>_<problem_name>.py` (e.g. `36_valid_sudoku.py`). Each file contains:

1. **My solution** — a `Solution` class written from scratch, plus a small `__main__` block with test cases.
2. **A review at the top of the file**, in the module docstring, written with Claude Code. It covers:
   - whether my solution is correct,
   - its time / space complexity,
   - observations on efficiency and idiom (what to change and why),
   - a suggested reference implementation.

My code below the docstring is left untouched — the review only ever *adds* the docstring, so the original attempt stays visible for comparison.

## Files

| File | Problem | Difficulty |
| --- | --- | --- |
| `36_valid_sudoku.py` | [36. Valid Sudoku](PROBLEMS_STATEMENTS.md#36-valid-sudoku) | Medium |
| `48_rotate_image.py` | [48. Rotate Image](PROBLEMS_STATEMENTS.md#48-rotate-image) | Medium |
| `70_climbing_stairs.py` | [70. Climbing Stairs](PROBLEMS_STATEMENTS.md#70-climbing-stairs) | Easy |
| `74_search_a_2d_matrix.py` | [74. Search a 2D Matrix](PROBLEMS_STATEMENTS.md#74-search-a-2d-matrix) | Medium |
| `88_merge_sorted_array.py` | [88. Merge Sorted Array](PROBLEMS_STATEMENTS.md#88-merge-sorted-array) | Easy |
| `121_best_time_to_buy_and_sell_a_stock.py` | [121. Best Time to Buy and Sell Stock](PROBLEMS_STATEMENTS.md#121-best-time-to-buy-and-sell-stock) | Easy |
| `122_best_time_to_buy_and_sell_a_stock.py` | [122. Best Time to Buy and Sell Stock II](PROBLEMS_STATEMENTS.md#122-best-time-to-buy-and-sell-stock-ii) | Medium |
| `125_valid_palindrome.py` | [125. Valid Palindrome](PROBLEMS_STATEMENTS.md#125-valid-palindrome) | Easy |
| `162_find_peak_element.py` | [162. Find Peak Element](PROBLEMS_STATEMENTS.md#162-find-peak-element) | Medium |

Full problem statements are collected in [`PROBLEMS_STATEMENTS.md`](PROBLEMS_STATEMENTS.md).

## Running

Each file is self-contained and runs its own assertions:

```bash
python 36_valid_sudoku.py
```

Requires Python 3.9+ (uses `typing.List` annotations; standard library only).

## Adding a new problem

1. Create `<number>_<problem_name>.py` with a `Solution` class and a `__main__` block of test cases.
2. Ask Claude Code to review it and add the docstring summary.
3. Append the problem statement to `PROBLEMS_STATEMENTS.md` and a row to the table above.
