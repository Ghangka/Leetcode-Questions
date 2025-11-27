#  https://neetcode.io/problems/max-area-of-island?list=neetcode150

# Runtime: O(m*n)
# Space: O(m*n)

import collections
from typing import List

class Solution:
    def max_area_of_island(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def bfs(r,c):
            area = 1
            queue = collections.deque()
            queue.append((r,c))
            visit.add((r,c))
            directions = [[0,1],[0,-1], [1,0], [-1,0]]

            while len(queue) > 0:
                row, col = queue.popleft()
                print(len(queue))
                # break

                for dr, dc in directions:
                    new_r = dr + row
                    new_c = dc + col

                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == 1 and (new_r,new_c) not in visit:
                        queue.append((new_r, new_c))
                        visit.add((new_r, new_c))
                        area +=1
                        # break
           
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = bfs(r,c)
                    print("area", area)
                    max_area = max(area, max_area)
        
        return max_area

        