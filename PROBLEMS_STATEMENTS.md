# Problem Statements

Reconstructed from LeetCode. Solutions live in the correspondingly named
`.py` files.

---

## 36. Valid Sudoku

**Difficulty:** Medium — `36_valid_sudoku.py`

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be
validated **according to the following rules**:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9`
  without repetition.

**Note:**

- A Sudoku board (partially filled) could be valid but is not necessarily
solvable.
- Only the filled cells need to be validated according to the mentioned rules.

### Example 1

```
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

### Example 2

```
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is
invalid.
```

### Constraints

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `1-9` or `'.'`.

---

## 48. Rotate Image

**Difficulty:** Medium — `48_rotate_image.py`

You are given an `n x n` 2D `matrix` representing an image, rotate the image by
**90 degrees (clockwise)**.

You have to rotate the image [in-place](https://en.wikipedia.org/wiki/In-place_algorithm),
which means you have to modify the input 2D matrix directly. **DO NOT** allocate
another 2D matrix and do the rotation.

### Example 1

```
Input:  matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

### Example 2

```
Input:  matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

### Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

---

## 70. Climbing Stairs

**Difficulty:** Easy — `70_climbing_stairs.py`

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can
you climb to the top?

### Example 1

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

### Example 2

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

### Constraints

- `1 <= n <= 45`

---

## 74. Search a 2D Matrix

**Difficulty:** Medium — `74_search_a_2d_matrix.py`

You are given an `m x n` integer matrix `matrix` with the following two
properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the
  previous row.

Given an integer `target`, return `true` if `target` is in `matrix`, or `false`
otherwise.

You must write a solution in `O(log(m * n))` time complexity.

### Example 1

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

### Example 2

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

### Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4`

---

## 88. Merge Sorted Array

**Difficulty:** Easy — `88_merge_sorted_array.py`

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing
order, and two integers `m` and `n`, representing the number of elements in
`nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be
stored inside the array `nums1`. To accommodate this, `nums1` has a length of
`m + n`, where the first `m` elements denote the elements that should be
merged, and the last `n` elements are set to `0` and should be ignored.
`nums2` has a length of `n`.

### Example 1

```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming
from nums1.
```

### Example 2

```
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
```

### Example 3

```
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there
to ensure the merge result can fit in nums1.
```

### Constraints

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

---

## 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy — `121_best_time_to_buy_and_sell_a_stock.py`

You are given an array `prices` where `prices[i]` is the price of a given stock
on the `i`th day.

You want to maximize your profit by choosing a **single day** to buy one stock
and choosing a **different day in the future** to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return `0`.

### Example 1

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must
buy before you sell.
```

### Example 2

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

### Constraints

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

---

## 122. Best Time to Buy and Sell Stock II

**Difficulty:** Medium — `122_best_time_to_buy_and_sell_a_stock.py`

You are given an integer array `prices` where `prices[i]` is the price of a
given stock on the `i`th day.

On each day, you may decide to buy and/or sell the stock. You can only hold
**at most one** share of the stock at any time. However, you can buy it then
immediately sell it on the **same day**.

Find and return the maximum profit you can achieve.

### Example 1

```
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
```

### Example 2

```
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
```

### Example 3

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the
stock to achieve the maximum profit of 0.
```

### Constraints

- `1 <= prices.length <= 3 * 10^4`
- `0 <= prices[i] <= 10^4`

---

## 125. Valid Palindrome

**Difficulty:** Easy — `125_valid_palindrome.py`

A phrase is a **palindrome** if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads the
same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

### Example 1

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

### Example 2

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

### Example 3

```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

### Constraints

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

---

## 162. Find Peak Element

**Difficulty:** Medium — `162_find_peak_element.py`

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array `nums`, find a peak element, and return its
index. If the array contains multiple peaks, return the index to **any** of
the peaks.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is
always considered to be strictly greater than a neighbor that is outside the
array.

You must write an algorithm that runs in `O(log n)` time.

### Example 1

```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

### Example 2

```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak
element is 2, or index number 5 where the peak element is 6.
```

### Constraints

- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `nums[i] != nums[i + 1]` for all valid `i`.
