# https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree?list=neetcode150

# Runtime: O(n) where n is the height of the Tree
# Space: O(1)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return root
        
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr


        # First Draft:

        # queue = []
        # queue.append(root)

        # while len(queue) > 0:
        #     node = queue.pop(0)
        
        #     if node is None or node.left is None or node.right is None:
        #         continue
        #     print(" node: ", node.val)
        #     # case where the ancestor is a parent of the other node
        #     if node.val == p.val and (node.left.val == q.val or node.right.val == q.val):
        #         print("here")
        #         return node
        #     if node.val == q.val and (node.left.val == p.val or node.right.val == p.val):
        #         return node
            
        #     # case where current node is the LCA
        #     if node.left.val == q.val and node.right.val == p.val:
        #         return node
        #     if node.left.val == p.val and node.right.val == q.val:
        #         return node
        #     queue.append(node.left)
        #     queue.append(node.right)

        # return root


