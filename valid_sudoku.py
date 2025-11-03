# https://leetcode.com/problems/valid-sudoku/
# O(n^2) time complexity
# O(n) space complexity
class Solution:
    def is_valid_sudoku(self, board: list[list[str]]) -> bool:
        # Row case
        for r in range(len(board)):
            rowMap = {}
            for c in board[r]:
                if c == ".":
                    continue
                if c in rowMap:
                    return False
                else:
                    rowMap[c] = True
        
        # Column case
        for c in range(len(board)):
            colMap = {}
            for r in range(len(board)):
                if board[r][c] == ".":
                    continue
                if board[r][c] in colMap:
                    return False
                else:
                    colMap[board[r][c]] = True
        
        # Sub-box case
        for r in range(0, len(board), 3):
            for c in range(0, len(board), 3):
                i = r
                j = c
                map = {}
                for i in range(3):
                    for j in range(3):
                        if board[r+i][c+j] == ".":
                            continue
                        if board[r+i][c+j] in map:
                            return False
                        else:
                            map[board[r+i][c+j]] = True
        return True