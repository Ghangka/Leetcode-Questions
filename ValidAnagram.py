# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n log n) time complexity
        # O(1) space complexity
        # if len(s) != len(t):
        #     return False
        
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False


        # O(n) time complexity
        # O(n) space complexity
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT