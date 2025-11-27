# https://neetcode.io/problems/binary-tree-maximum-path-sum/question?list=blind75 

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Had to look at solution to solve this problem.
# Runtime: O(n)
# Space: O(n)
class BinaryTree:
    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            left_max = dfs(root.left)
            right_max = dfs(root.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            res[0] = max(res[0], root.val + left_max + right_max)
            return root.val + max(left_max, right_max)

        dfs(root)
        return res[0]