# https://neetcode.io/problems/pacific-atlantic-water-flow/question?list=blind75

from typing import List

# Pacific -> (0,0) -> (0, COLS -1) , (0,0) -> (ROWS - 1, 0)
# Atlantic -> (0, COLS - 1) -> (ROWS - 1, COLS-1 ) , (ROWS - 1, 0) -> (ROWS - 1, COLS - 1)

# Runtime: O(m*n)
# Space: O(m*n)
# where m is the number of rows and n is the number of columns

class Islands:
    def find_islands(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        visit = set()
        pac, atl = set(), set()

        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs (r, c , visit, prev_height):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or heights[r][c] < prev_height:
                return

            visit.add((r,c))

            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r, c])
        return result