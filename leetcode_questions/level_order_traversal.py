# https://neetcode.io/problems/level-order-traversal-of-binary-tree?list=neetcode150

# Runtime: O(n)
# Space: O(n) -> O(2n) - 2 arrays of length n max, simplifies to O(n)

# Definition for a binary tree node.
from ast import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = []
        queue.append(root)
        
        result = []

        while len(queue) > 0:
            level_size = len(queue)
            curr_list = []
            
            for _ in range(level_size):
                node = queue.pop(0)
                curr_list.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            result.append(curr_list)

        return result

        