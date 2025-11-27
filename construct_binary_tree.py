# https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal/question?list=blind75

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Had to look at solution to solve this question.
# Runtime: O(n^2)
# Space: O(1)
class BinaryTree:
    def build_tree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.build_tree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.build_tree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root