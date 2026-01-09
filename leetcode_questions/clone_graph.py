# https://neetcode.io/problems/clone-graph/question?list=blind75

# Definition for a Node.
from typing import Optional

# Runtime: O(V + E)
# Space: O(V)
# where V is the number of vertices and E is the number of edges
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class CloneGraph:
    def clone(self, node:Optional[Node]) -> Optional[Node]:
        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            
            copy = Node(node.val)
            old_to_new[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None