# https://neetcode.io/problems/level-order-traversal-of-binary-tree?list=neetcode150

# Runtime: O(n)
# Space: O(2n) - 2 arrays of length n max

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
        result.append([root.val])

        while len(queue) > 0:
            curr_queue = queue.copy() 
            # curr_queue = queue
            curr_list = []

            while len(curr_queue) > 0:
                curr = curr_queue.pop(0)
                # print("queue, curr, curr_queue", queue, curr, curr_queue)
                pop = queue.pop(0)

                if curr is None:
                    continue
                
                if curr.left is not None:
                    curr_list.append(curr.left.val)
                    queue.append(curr.left)
                if curr.right is not None:
                    curr_list.append(curr.right.val)
                    queue.append(curr.right)
            
            if len(curr_list) != 0:
                result.append(curr_list)

        return result

        