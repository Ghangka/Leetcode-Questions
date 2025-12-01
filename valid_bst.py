import collections
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Runtime: O(n) -> need to visit every node
# Space: O(n) -> queue has max length of nodes in the tree 
class BST:
    def is_valid(self, root:Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = collections.deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))

        return True