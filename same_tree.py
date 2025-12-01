# https://leetcode.com/problems/same-tree/
# O(n) time complexity
# O(n) space complexity

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        queue_p = []
        queue_q = []
        visited_nodes = {}

        queue_p.append(p)
        queue_q.append(q)

        while len(queue_p) > 0:
            node_p = queue_p.pop(0)
            node_q = queue_q.pop(0)

            print("nodes",node_p, node_q)

            if node_p.val != node_q.val:
                return False
            
            if node_p not in visited_nodes:
                visited_nodes[node_p] = True
                if node_p.left is not None and node_q.left is not None:
                    queue_p.append(node_p.left)
                    queue_q.append(node_q.left)
                if node_p.right is not None and node_q.right is not None:
                    queue_p.append(node_p.right)
                    queue_q.append(node_q.right)
                if (node_p.right is None) != (node_q.right is None):
                    return False
                if (node_p.left is None) != (node_q.left is None):
                    return False

        return True
        