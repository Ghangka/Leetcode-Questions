# https://neetcode.io/problems/design-word-search-data-structure/question?list=blind75

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    # Runtime: O(n)
    # Space: O(n)
    def add_word(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.end_of_word = True

    # Runtime: O(n)
    # Space: O(n)
    def search_word(self, word: str) -> bool:

        def dfs(j, root):
            curr = root
            
            for i in range(j , len(word)):
                c = word[i]

                if c == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            
            return curr.end_of_word
        
        return dfs(0, self.root)
        
