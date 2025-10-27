# https://leetcode.com/problems/contains-duplicate/
# O(n) time complexity
# O(n) space complexity

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:

        hashMap = {}

        for num in nums:
            if hashMap.get(num) is None:
                hashMap[num] = True
            else:
                return True

        return False
        