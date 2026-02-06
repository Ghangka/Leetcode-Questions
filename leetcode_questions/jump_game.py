# https://neetcode.io/problems/jump-game/question?list=blind75

from typing import List

# Runtime: O(n)
# Space: O(1)

class Solution:
    def can_jump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1 , -1):
            if nums[i] + i >= goal:
                goal = i
        
        if goal == 0:
            return True
        else:
            return False