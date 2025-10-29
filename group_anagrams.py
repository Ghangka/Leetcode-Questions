# https://leetcode.com/problems/group-anagrams/
# O(n * m) time complexity
# O(n) space complexity

class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26

            for c in s:
                # mapping characters to index in alphabet
                count[ord(c) - ord('a')] += 1
            # lists can't be keys for dictionaries (lists are mutable), so we convert to tuple
            res[tuple(count)].append(s)

        # return only the values of the dictionary
        return list(res.values())