# https://neetcode.io/problems/count-number-of-islands?list=neetcode150

# Runtime: O(m*n)
# Space: O(m*n)

import collections
from typing import List

class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            queue = collections.deque()
            visit.add((r,c))
            queue.append((r,c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1" and (nr,nc) not in visit:
                        queue.append((nr,nc))
                        visit.add((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands +=1

        return islands