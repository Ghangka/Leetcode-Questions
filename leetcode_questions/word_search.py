# https://neetcode.io/problems/search-for-word/question?list=blind75
from typing import List

# Runtime: O(n * m * 4^l)
# Space: O(l)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        # Keep track of the path to avoid revisiting the same cell
        path = set()

        def dfs(r, c, i):
            # If we have found the word, return True
            if i == len(word):
                return True

            # If the current cell is out of bounds or the current character does not match the word, return False
            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            # Add the current cell to the path
            path.add((r, c))

            # Recursively search for the next character
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            # Remove the current cell from the path
            path.remove((r, c))
            return res

        # Iterate through the board and start the search from each cell
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False
