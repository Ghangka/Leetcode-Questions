import collections
from typing import Optional
import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Runtime: O(n + k log n) due to heapify and heappop
# Space: O(n) where n is the number of nodes in the tree
class BST:
    def kth_smallest(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return -1
        
        heap = []
        queue = collections.deque()
        queue.append(root)

        while len(queue) > 0:
            curr = queue.popleft()
            if curr is None:
                continue
            heap.append(curr.val)
            queue.append(curr.left)
            queue.append(curr.right)

        heapq.heapify(heap)

        while k > 1:
            print(heap)
            heapq.heappop(heap)
            k -= 1
        
        return heap[0]