# https://neetcode.io/problems/search-for-word-ii/question?list=blind75
from typing import List

# Runtime: O(M*N * 4^L) where M*N = board size, L = max word length.
#   Trie build: O(W*L) for W words. DFS from each cell: O(M*N) starts × up to 4^L
#   paths per start (trie prunes invalid branches).
# Space: O(S + L) — S = total chars in trie (sum of word lengths), L = recursion depth.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word: str):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

class WordSearch2:
    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])

        root = TrieNode()

        for w in words:
            root.add_word(w)
        
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or board[r][c] not in node.children):
                return

            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.is_word:
                res.add(word)

            dfs( r + 1, c, node, word)
            dfs( r - 1, c, node, word)
            dfs( r, c + 1, node, word)
            dfs( r, c - 1, node, word)

            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)