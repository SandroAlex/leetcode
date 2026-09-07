# LeetCode Studies

A personal study log of LeetCode problems. For each problem I write my own solution first, then use **Claude Code** to review it and produce a reference ("best practice") version, and I keep both side by side so I can see the gap and learn from it.

## How it works

For every problem there is one Python file, named after the problem (e.g. `valid_sudoku.py`). Each file contains:

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
| `climbing_stairs.py` | [70. Climbing Stairs](PROBLEMS_STATEMENTS.md#70-climbing-stairs) | Easy |
| `valid_sudoku.py` | [36. Valid Sudoku](PROBLEMS_STATEMENTS.md#36-valid-sudoku) | Medium |
| `rotate_image.py` | [48. Rotate Image](PROBLEMS_STATEMENTS.md#48-rotate-image) | Medium |

Full problem statements are collected in [`PROBLEMS_STATEMENTS.md`](PROBLEMS_STATEMENTS.md).

## Running

Each file is self-contained and runs its own assertions:

```bash
python valid_sudoku.py
```

Requires Python 3.9+ (uses `typing.List` annotations; standard library only).

## Adding a new problem

1. Create `<problem_name>.py` with a `Solution` class and a `__main__` block of test cases.
2. Ask Claude Code to review it and add the docstring summary.
3. Append the problem statement to `PROBLEMS_STATEMENTS.md` and a row to the table above.
