"""
Maximum Depth of Binary Tree - solution review
==============================================

Correct - verified both by hand-tracing and now by the test suite's own
assertions (depths 3 and 4). O(n) time (every node is visited once) and O(h)
extra space for the recursion stack, where h is the tree's height - the same
complexity class as the standard solution.

Observations
------------
1. The leaf special case is only needed because this version avoids recursing
   into a `None` child. The canonical formulation recurses into both children
   unconditionally (a `None` child returns 0 immediately) and always adds 1
   for the current node, so a leaf falls out of the general case for free:
   `1 + max(maxDepth(None), maxDepth(None)) == 1`. Here, skipping the call
   when a child is `None` means neither `left_path` nor `right_path` gets a
   "+1 for me" when both children are absent, so the leaf case has to be
   special-cased to avoid returning 0 for a single node. It is a reasonable
   micro-optimization (two fewer no-op calls per leaf) but it is what forces
   the extra branch.
2. `CurNode` uses PascalCase, which reads as a class name; the rest of the
   file (and repo) uses snake_case for variables. It is also just an alias
   for `root` - not needed.
3. Recursion depth is a real risk here, not just a style note: the problem's
   own constraints allow up to 10^4 nodes, and a maximally skewed (linked-list
   shaped) tree needs that many nested recursive calls. Python's default
   recursion limit is ~1000, so a valid, constraint-satisfying input can raise
   `RecursionError` in Python even though the algorithm is correct - the
   iterative revision below sidesteps this entirely.

Suggested revision - tidied recursive form
-------------------------------------------
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

Suggested revision - iterative (avoids Python's recursion limit)
-------------------------------------------------------------------
    from collections import deque

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 0
        queue = deque([root])
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth

Level-order (BFS) traversal counting levels: same O(n) time, O(w) space (w is
the tree's maximum width) instead of O(h) on the call stack - no recursion at
all, so it is safe regardless of how deep or skewed the tree is.
"""

from __future__ import annotations
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:

        # Initialize at the root of the tree
        CurNode: TreeNode = root

        # Trivial case
        if CurNode is None:
            return 0

        # Initialize the returns
        right_path: int = 0
        left_path: int = 0

        # Base case: the node has not left neither right neighbours
        if (CurNode.left is None) and (CurNode.right is None):
            return 1

        # If left node exists, goes down the tree
        if CurNode.left is not None:

            # Update my current position
            left_path: int = 1 + self.maxDepth(root=CurNode.left)

        # if the right node exists, goes down the tree
        if CurNode.right is not None:

            # Update my current position
            right_path: int = 1 + self.maxDepth(root=CurNode.right)

        return max(left_path, right_path)


if __name__ == "__main__":

    # Test case 1
    leaf1: TreeNode = TreeNode(val=15)
    leaf2: TreeNode = TreeNode(val=7)
    node1: TreeNode = TreeNode(val=20, left=leaf1, right=leaf2)
    node2: TreeNode = TreeNode(val=9)
    root: TreeNode = TreeNode(val=3, left=node2, right=node1)
    sol: int = Solution().maxDepth(root=root)
    out: int = 3
    assert sol == out, "Test case 1 failed!"

    # Test case 2
    leaf2: TreeNode = TreeNode(val=9)
    node2: TreeNode = TreeNode(val=8, right=leaf2)
    node1: TreeNode = TreeNode(val=7, left=node2)
    leaf1: TreeNode = TreeNode(val=-1)
    root: TreeNode = TreeNode(val=6, left=leaf1, right=node1)
    sol: int = Solution().maxDepth(root=root)
    out: int = 4
    assert sol == out, "Test case 2 failed!"

    print(f">>> All test cases successfully run!")
